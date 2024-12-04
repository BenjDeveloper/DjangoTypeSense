from catalog.models import Category, Product

# Puedes ejecutar este script desde el shell de Django:
# python manage.py shell o shell_plus
# docker exec -it django_app python manage.py shell
# Luego copia y pega el script para ejecutarlo.

cat1 = Category.objects.create(name="Impresoras", description="Todo tipo de impresoras.")
cat2 = Category.objects.create(name="Etiquetas", description="Etiquetas de alta calidad para impresión.")

products = [
    Product(name=f"Producto {i}", description="Descripción del producto", price=100 + i, sku=f"SKU{i}", brand="Marca", category=cat1 if i % 2 == 0 else cat2)
    for i in range(1, 21)
]

Product.objects.bulk_create(products)



