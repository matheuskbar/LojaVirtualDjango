from django.contrib import admin

from orders.models import Order
from orders.models import Item


class ItemInline(admin.TabularInline):
    model = Item
    raw_id_fields = ['product']
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'name', 'email', 'paid', 'created', 'modified']
    list_filter = ['paid', 'created', 'modified']
    search_fields = ['name', 'cpf', 'email']
    inlines = [ItemInline]
