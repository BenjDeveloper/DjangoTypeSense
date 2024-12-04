from catalog.typesense_client import *


def test_search_products(query="impresoras"):
    # Llamada a la función para buscar productos relacionados con "impresora"
    resultado_busqueda = search_products(query) 

    # Verificar si se encontraron resultados
    if resultado_busqueda:
        print("Resultados de la búsqueda:")
        for hit in resultado_busqueda['hits']:
            producto = hit['document']
            print(f"Nombre: {producto['name']}, Marca: {producto['brand']}, Categoría: {producto['category']}")
    else:
        print("No se encontraron resultados.")


def test_get_all_products():
    # Llamada a la función para buscar productos relacionados con "impresora"
    resultado_busqueda = get_all_products() 

    # Verificar si se encontraron resultados
    if resultado_busqueda:
        print("Resultados de la búsqueda:")
        for hit in resultado_busqueda['hits']:
            producto = hit['document']
            print(f"Nombre: {producto['name']}, Marca: {producto['brand']}, Categoría: {producto['category']}")
    else:
        print("No se encontraron resultados.")

