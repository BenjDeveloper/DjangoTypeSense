from django.core.management.base import BaseCommand
from catalog.typesense_client import create_typesense_product_schema

class Command(BaseCommand):
    help = 'Crea el esquema del producto en Typesense'

    def handle(self, *args, **options):
        self.stdout.write("Creando esquema del producto en Typesense...")
        create_typesense_product_schema()
        self.stdout.write(self.style.SUCCESS('Esquema creado exitosamente.'))
