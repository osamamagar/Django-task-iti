from django.contrib import admin
from .models import Product


# class ProductAdmin(admin.ModelAdmin):
#     list_display = ('name', 'price', 'display_created_by', 'created_at', 'updated_at')

#     def display_created_by(self, obj):
#         return obj.created_by.username if obj.created_by else "N/A"

# admin.site.register(Product, ProductAdmin)


admin.site.register(Product)
