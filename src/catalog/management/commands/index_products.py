from django.core.management.base import BaseCommand
from catalog.models import Product
from catalog.typesense_client import index_product_in_typesense


class Command(BaseCommand):
    help = 'Indexa todos los productos en Typesense'

    def handle(self, *args, **kwargs):
        # Obtener todos los productos de la base de datos
        products = Product.objects.all()

        # Indexar los productos en Typesense
        for product in products:
            try:
                index_product_in_typesense(product)
                self.stdout.write(self.style.SUCCESS(f'Producto {product.name} indexado con éxito.'))
            except Exception as e:
                self.stdout.write(self.style.ERROR(f'Error al indexar el producto {product.name}: {e}'))
