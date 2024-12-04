from django.shortcuts import render
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Product
from .typesense_client import search_products, index_product_in_typesense


def search_view(request):
    query = request.GET.get('q')
    results = search_products(query)
    return render(request, 'catalog/search_results.html', {'results': results})


@receiver(post_save, sender=Product)
def index_product_signal(sender, instance, **kwargs):
    index_product_in_typesense(instance)