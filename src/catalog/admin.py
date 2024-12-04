from django.contrib import admin, messages
from .models import Product, Category
from .typesense_client import search_products


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'price', 'category') 
    search_fields = ('name', 'description', 'brand','category') 

    def get_search_results(self, request, queryset, search_term):
        if not search_term:
            return queryset, False
        
        try:
            results = search_products(search_term) 
            ids = [int(hit['document']['id']) for hit in results['hits']]
            return queryset.filter(id__in=ids), False 
        except Exception as e:
            self.message_user(request, f"Error de búsqueda: {e}", level=messages.ERROR)
            return queryset, False

admin.site.register(Product, ProductAdmin)


admin.site.register(Category)
#admin.site.register(Product)