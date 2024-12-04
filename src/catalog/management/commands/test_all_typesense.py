from django.core.management.base import BaseCommand
from catalog.scripts.test_typesense import test_search_products, test_get_all_products

# python manage.py test_all_typesense
# python manage.py test_all_typesense --query="impresoras"


class Command(BaseCommand):
    help = 'Prueba las funciones de búsqueda y obtención de productos en Typesense'

    def add_arguments(self, parser):
        parser.add_argument(
            '--query',
            type=str,
            help='Especifica el término de búsqueda para probar la función search_products',
        )

    def handle(self, *args, **kwargs):
        query = kwargs.get('query')

        # Si se pasa un argumento de búsqueda, ejecutar la búsqueda por el término proporcionado
        if query:
            self.stdout.write(self.style.SUCCESS('Probando la función test_search_products("query")'))
            self.stdout.write(self.style.SUCCESS(f'Buscando productos con el término: {query}'))
            test_search_products(query)
        else:
            # Si no se pasa un término, probar ambas funciones
            self.stdout.write(self.style.SUCCESS('Probando la función test_get_all_products()'))
            test_get_all_products()
