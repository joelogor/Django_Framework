from django.contrib import admin
from .models import Product, Category, Inventory, Cart, CartItem
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Register your models here.
@admin.register(Product)
class Product(admin.ModelAdmin):
    model = Product
    list_display = ['category', 'title', 'description', 'price', 'is_active']
    search_fields = ['title','category']
    list_filter = ['is_active', 'price']


@admin.register(Category)
class Category(admin.ModelAdmin):
    model = Category
    list_display = ['name', 'slug']
    search_fields = ['name']
    prepopulated_fields = {'slug':('name',)}

@admin.register(Inventory)
class Inventory(admin.ModelAdmin):
    model = Inventory
    list_display = ['product', 'quantity', 'quantity_on_hand', 'quantity_reserved', 'low_stock_threshold']
    search_fields = ['product']

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    model = Cart
    list_display = ['cart_id', 'created_at', 'updated_at', ]
    search_fields = ['cart_id']

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    model = CartItem
    list_display = ['cart', 'product', 'quantity', ]
    search_fields = ['cart', 'product']







