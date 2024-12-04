import typesense 
from django.conf import settings


# Configuración del cliente Typesense
client = typesense.Client(settings.TYPESENSE_CONFIG)


def get_typesense_client():
    return typesense.Client(settings.TYPESENSE_CONFIG)


def create_typesense_product_schema():
    schema = {
        'name': 'products',
        'fields': [
            {'name': 'name', 'type': 'string'},
            {'name': 'description', 'type': 'string'},
            {'name': 'price', 'type': 'float'},
            {'name': 'category', 'type': 'string'},
            {'name': 'sku', 'type': 'string'},
            {'name': 'brand', 'type': 'string'},
        ],
        'default_sorting_field': 'price'
    }
    try:
        client.collections.create(schema)
        print("Schema creado exitosamente.")
    except typesense.exceptions.ObjectAlreadyExists:
        print("El schema ya existe.")


# Función para indexar un producto en Typesense
def index_product_in_typesense(product):
    document = {
        'name': product.name,
        'description': product.description,
        'price': float(product.price),
        'category': product.category.name,
        'sku': product.sku,
        'brand': product.brand,
    }
    try:
        client.collections['products'].documents.upsert(document)
        print(f"Producto '{product.name}' indexado exitosamente.")
    except Exception as e:
        print(f"Error al indexar el producto: {e}")


# Función para realizar búsquedas en el índice de Typesense
def search_products(query):
    try:
        search_parameters = {
            'q': query,
            'query_by': 'name,description,brand,category'
        }
        results = client.collections['products'].documents.search(search_parameters)
        return results
    except Exception as e:
        print(f"Error durante la búsqueda: {e}")
        return None


# Función para obtener todos los productos de la colección de Typesense
def get_all_products():
    try:
        # Parámetros de búsqueda para obtener todos los productos
        search_parameters = {
            'q': '*',  # '*' para obtener todos los documentos
            'query_by': 'name,description,brand,category',  # Campos donde buscar
            'per_page': 250,  # Máximo de resultados por página (puede ser ajustado)
            'page': 1  # Página inicial
        }

        # Realizar la búsqueda inicial
        results = client.collections['products'].documents.search(search_parameters)

        # Obtener todos los resultados si hay paginación
        all_results = results['hits']
        total_pages = results['found'] // 250 + (1 if results['found'] % 250 > 0 else 0)

        # Iterar sobre cada página para obtener todos los documentos si es necesario
        for page in range(2, total_pages + 1):
            search_parameters['page'] = page
            next_page_results = client.collections['products'].documents.search(search_parameters)
            all_results.extend(next_page_results['hits'])

        return results
    except Exception as e:
        print(f"Error durante la obtención de todos los productos: {e}")
        return None