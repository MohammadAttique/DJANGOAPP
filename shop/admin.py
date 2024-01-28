from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'discounted_price', 'stock_quantity', 'brand', 'category')
    search_fields = ('name', 'brand__name', 'category__name')
    list_filter = ('brand', 'category')
    readonly_fields = ('formatted_price',)
    fieldsets = (
        ('General Information', {
            'fields': ('name', 'description', 'image')
        }),
        ('Pricing Information', {
            'fields': ('price', 'discounted_price', 'formatted_price')
        }),
        ('Stock Information', {
            'fields': ('stock_quantity',)
        }),
        ('Categorization', {
            'fields': ('brand', 'category')
        }),
    )
