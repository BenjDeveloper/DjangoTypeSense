from django.core.management.base import BaseCommand
from catalog.typesense_client import get_typesense_client

class Command(BaseCommand):
    help = 'Lista todos los esquemas de colecciones en el servidor de Typesense.'

    def handle(self, *args, **options):
        client = get_typesense_client()
        try:
            collections = client.collections.retrieve()
            if collections:
                self.stdout.write(self.style.SUCCESS('Esquemas de colecciones en Typesense:'))
                for collection in collections:
                    self.stdout.write(f'Nombre: {collection["name"]}, Campos: {collection["fields"]}')
            else:
                self.stdout.write(self.style.WARNING('No hay colecciones configuradas en Typesense.'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error al recuperar colecciones: {e}'))
