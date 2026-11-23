from django.contrib import admin
from.models import Order, OrderItem
# Register your models here.

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    model = Order
    list_display = ['user', 'status', 'shipping_address', 'total', 'created_at']
    search_fields = ['user', 'shipping_address', 'total', 'created_at']

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    model = OrderItem
    list_display = ['order', 'product', 'quantity', 'price']
    search_fields = ['order', 'product']