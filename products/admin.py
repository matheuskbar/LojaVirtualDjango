from django.contrib import admin

from .models import Category, Product


# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'created', 'modified']
    list_filter = ['is_available', ]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', ]
