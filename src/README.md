# Ecommerce Django con Typesense

Este proyecto es una aplicación de ecommerce desarrollada con Django, que utiliza Typesense para proporcionar capacidades de búsqueda mejoradas. El sistema permite a los usuarios buscar productos por nombre, descripción, marca y categoría, ofreciendo resultados relevantes y rápidos.

## Pre-requisitos

Antes de comenzar, asegúrate de tener instalado:
- Python 3.10 o superior
- Django 3.2 o superior
- Docker y Docker Compose

## Configuración del Entorno

Clona el repositorio y configura el entorno de desarrollo:

bash
git clone https://github.com/tu_usuario/tu_proyecto_ecommerce.git
cd tu_proyecto_ecommerce
pip install -r requirements.txt


## COMPONENTES PRINCIPALES

Backend Framework: 
 - Utiliza Django como el framework principal para manejar la lógica del backend
Modelos de Datos: 
- Incluye modelos como Product y Category, donde cada producto está asociado a una categoría.
Typesense:
- Motor de Búsqueda
- Indexación de Datos
Personalización del Admin: 
- Modificado para integrar la búsqueda de Typesense directamente en la lista de productos, reemplazando la búsqueda por defecto de Django.
Filtros y Búsqueda Avanzada: 
- Implementación de filtros personalizados basados en los datos devueltos por Typesense para mejorar la gestión de los productos.
Contenerización:
- Uso de Docker para asegurar un entorno de desarrollo y despliegue consistente, facilitando la portabilidad y la escalabilidad del proyecto.


## LEVANTAMIENTO DE PROYECTO 

Construir y Levantar los Contenedores con Docker Compose
Se Usa Docker Compose para construir y levantar los servicios definidos en tu docker-compose.yml. Esto incluirá tu aplicación Django, una base de datos Postgres, el servidor Typesense y librerias externas para su uso interno dentro del proyecto para su desarrollo y pruebas.

Crea y levanta los contenedores
 - docker-compose up --build

Migracion de los modelos a la Base de Datos
 - docker exec -it django_app python manage.py migrate

Creacion de super Usuario para el uso del admin para visualizacion del filtrado de productos con typesense
- docker exec -it django_app python manage.py createsuperuser


comandos perdonalizazados para agilizar las pruebas 
 - docker exec -it django_app python manage.py
...
[catalog]
    create_typesense_schema
    index_products
    load_sample_data
    remove_duplicate_products
    test_all_typesense
...

Carga de Datos sacados de  la web de logiscenter como modelo referencial ( https://www.logiscenter.com/ )
 - docker exec -it django_app python manage.py load_sample_data

Creacion de los esquemas en typesense
 - docker exec -it django_app python manage.py create_typesense_schema

Indexacion de los productos alojados en laz Base de Datos (postgresql)
 - docker exec -it django_app python manage.py index_products


TEST - TERMINAL 

Tambien se puede probar por terminal el fltrado por medio del uso del comando para falicitar la busqueda y filtrado de la informacion a nivel de backend por terminal 
 - docker exec -it django_app python manage.py test_all_typesense --query="Impresoras"
 - docker exec -it django_app python manage.py test_all_typesense --query="Impr"
 - docker exec -it django_app python manage.py test_all_typesense --query=""