from django.core.management.base import BaseCommand
from catalog.typesense_client import client

class Command(BaseCommand):
    help = 'Elimina productos duplicados indexados en Typesense'

    def handle(self, *args, **kwargs):
        try:
            search_parameters = {
                'q': '*',
                'query_by': 'name,description,brand,category,sku',
                'per_page': 250,
                'page': 1
            }

            results = client.collections['products'].documents.search(search_parameters)
            all_products = results['hits']
            total_pages = results['found'] // 250 + (1 if results['found'] % 250 > 0 else 0)

            for page in range(2, total_pages + 1):
                search_parameters['page'] = page
                next_page_results = client.collections['products'].documents.search(search_parameters)
                all_products.extend(next_page_results['hits'])

            unique_products = {}
            duplicates = []

            for hit in all_products:
                product = hit['document']
                identifier = (product['name'], product['sku'])

                if identifier in unique_products:
                    duplicates.append(product['id'])
                else:
                    unique_products[identifier] = product['id']

            if duplicates:
                self.stdout.write(self.style.WARNING(f'Encontrados {len(duplicates)} productos duplicados. Eliminando...'))
                for duplicate_id in duplicates:
                    try:
                        client.collections['products'].documents[duplicate_id].delete()
                        self.stdout.write(self.style.SUCCESS(f'Producto con ID {duplicate_id} eliminado correctamente.'))
                    except Exception as e:
                        self.stdout.write(self.style.ERROR(f'Error al eliminar el producto con ID {duplicate_id}: {e}'))
            else:
                self.stdout.write(self.style.SUCCESS('No se encontraron productos duplicados.'))

        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error durante la eliminación de productos duplicados: {e}'))
