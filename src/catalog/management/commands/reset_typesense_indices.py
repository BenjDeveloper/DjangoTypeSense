from django.core.management.base import BaseCommand
from catalog.typesense_client import get_typesense_client

class Command(BaseCommand):
    help = 'Elimina todos los índices y esquemas en el servidor de Typesense, dejando el servidor completamente limpio.'

    def handle(self, *args, **options):
        client = get_typesense_client()
        collections = client.collections.retrieve()

        # Eliminar todas las colecciones existentes
        for collection in collections:
            self.stdout.write(self.style.NOTICE(f'Eliminando colección: {collection["name"]}'))
            client.collections[collection['name']].delete()

        # Confirmar que todas las colecciones han sido eliminadas
        collections = client.collections.retrieve()
        if len(collections) == 0:
            self.stdout.write(self.style.SUCCESS('Todas las colecciones han sido eliminadas correctamente.'))
        else:
            self.stdout.write(self.style.ERROR('Algunas colecciones no se han eliminado correctamente.'))

        self.stdout.write(self.style.SUCCESS('El servidor de Typesense ha sido limpiado completamente.'))
