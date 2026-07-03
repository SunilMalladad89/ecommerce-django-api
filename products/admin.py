from django.contrib import admin
from .models import Product,Category, Profile, Order



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']
    search_fields = ['name']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'stock', 'created_at']
    list_display        = ['name', 'price', 'stock', 'created_at']
    list_display_links  = ['name']
    search_fields       = ['name', 'description']
    list_filter         = ['created_at']
    list_editable       = ['price', 'stock']
    list_per_page       = 10
    ordering            = ['-created_at']
    readonly_fields     = ['created_at', 'updated_at']
    fieldsets = [
        ('Product Information', {
            'fields': ['name', 'description','category','image']
        }),
        ('Pricing & Stock', {
            'fields': ['price', 'stock']
        }),
        ('Timestamps', {
            'fields': ['created_at', 'updated_at']
        }),
    ]


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'phone']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'created_at']
