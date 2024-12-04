from django.core.management.base import BaseCommand
from catalog.models import Category, Product

class Command(BaseCommand):
    help = 'Carga categorías y productos de ejemplo en la base de datos.'

    def handle(self, *args, **kwargs):
        # Definir las categorías basadas en las secciones principales de Logiscenter
        categories = [
            {"name": "Impresoras", "description": "Impresoras de etiquetas, tarjetas, tickets y más."},
            {"name": "Lectores", "description": "Lectores de códigos de barras y RFID."},
            {"name": "Terminales PDAs y Tablets", "description": "Dispositivos móviles para captura de datos."},
            {"name": "Consumibles", "description": "Etiquetas, ribbons, tarjetas y otros consumibles."},
            {"name": "Terminal Punto de Venta", "description": "Equipos y accesorios para puntos de venta."},
            {"name": "RF Wireless", "description": "Soluciones de conectividad inalámbrica."},
            {"name": "Software", "description": "Aplicaciones para diseño y gestión de códigos de barras y más."},
        ]

        # Crear las categorías en la base de datos
        created_categories = {}
        for category_data in categories:
            category, _ = Category.objects.get_or_create(**category_data)
            created_categories[category_data["name"]] = category

        self.stdout.write(self.style.SUCCESS("Categorías creadas exitosamente."))

        # Crear productos de ejemplo para cada categoría
        products = [
            # Productos para la categoría "Impresoras"
            {"name": "Impresora de Etiquetas Zebra ZD421", "description": "Impresora de etiquetas de alto rendimiento.", "price": 350.00, "sku": "IMP-ZD421", "brand": "Zebra", "category": created_categories["Impresoras"]},
            {"name": "Impresora de Tarjetas Datacard SD360", "description": "Impresora de tarjetas plásticas a doble cara.", "price": 1200.00, "sku": "IMP-SD360", "brand": "Datacard", "category": created_categories["Impresoras"]},
            {"name": "Impresora de Tickets Epson TM-T88VI", "description": "Impresora térmica de tickets de alta velocidad.", "price": 400.00, "sku": "IMP-T88VI", "brand": "Epson", "category": created_categories["Impresoras"]},
            {"name": "Impresora Portátil Zebra ZQ620", "description": "Impresora portátil para etiquetas y recibos.", "price": 600.00, "sku": "IMP-ZQ620", "brand": "Zebra", "category": created_categories["Impresoras"]},
            {"name": "Impresora de Pulseras Zebra ZD510-HC", "description": "Impresora especializada en pulseras para entornos sanitarios.", "price": 500.00, "sku": "IMP-ZD510", "brand": "Zebra", "category": created_categories["Impresoras"]},

            # Productos para la categoría "Lectores"
            {"name": "Lector de Códigos de Barras Datalogic QuickScan QD2430", "description": "Lector 2D de mano con cable.", "price": 150.00, "sku": "LEC-QD2430", "brand": "Datalogic", "category": created_categories["Lectores"]},
            {"name": "Lector Inalámbrico Zebra DS2278", "description": "Lector 2D inalámbrico con Bluetooth.", "price": 250.00, "sku": "LEC-DS2278", "brand": "Zebra", "category": created_categories["Lectores"]},
            {"name": "Lector RFID Impinj Speedway R420", "description": "Lector RFID fijo de alto rendimiento.", "price": 1500.00, "sku": "LEC-R420", "brand": "Impinj", "category": created_categories["Lectores"]},
            {"name": "Lector de Tarjetas Magnéticas MagTek SureSwipe", "description": "Lector de tarjetas magnéticas de doble cabezal.", "price": 100.00, "sku": "LEC-SureSwipe", "brand": "MagTek", "category": created_categories["Lectores"]},
            {"name": "Lector de Códigos de Barras Honeywell Voyager 1250g", "description": "Lector láser de mano con cable.", "price": 130.00, "sku": "LEC-1250G", "brand": "Honeywell", "category": created_categories["Lectores"]},

            # Productos para la categoría "Terminales PDAs y Tablets"
            {"name": "PDA Zebra TC52", "description": "Terminal táctil robusto con Android.", "price": 900.00, "sku": "PDA-TC52", "brand": "Zebra", "category": created_categories["Terminales PDAs y Tablets"]},
            {"name": "Tablet Industrial Getac F110", "description": "Tablet robusta de 11.6 pulgadas.", "price": 2000.00, "sku": "TAB-F110", "brand": "Getac", "category": created_categories["Terminales PDAs y Tablets"]},
            {"name": "PDA Honeywell Dolphin CT60", "description": "Terminal móvil empresarial con 4G LTE.", "price": 950.00, "sku": "PDA-CT60", "brand": "Honeywell", "category": created_categories["Terminales PDAs y Tablets"]},
            {"name": "Tablet Rugerizada Zebra ET56", "description": "Tablet ligera y resistente para uso industrial.", "price": 1500.00, "sku": "TAB-ET56", "brand": "Zebra", "category": created_categories["Terminales PDAs y Tablets"]},
            {"name": "PDA Datalogic Memor 10", "description": "Dispositivo móvil compacto con Android.", "price": 850.00, "sku": "PDA-Memor10", "brand": "Datalogic", "category": created_categories["Terminales PDAs y Tablets"]},
        ]

        product_instances = [Product(**product_data) for product_data in products]

        Product.objects.bulk_create(product_instances)

        self.stdout.write(self.style.SUCCESS("Productos creados exitosamente."))
