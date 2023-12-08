from django.contrib import admin
from .models import UserProfile, Product, Inventory, Cart, CartItem, Order, OrderDetails, Receipt

# Register your models here.

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'dob', 'phone_number', 'address')
    search_fields = ('user__username', 'phone_number')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'quantity_available', 'serial_number', 'category')
    search_fields = ('name', 'category', 'serial_number')

@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    list_display = ('product', 'location')
    search_fields = ('product__name', 'location')

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('user',)
    search_fields = ('user__username',)

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('cart', 'product', 'total_quantity')
    search_fields = ('cart__user__username', 'product__name')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'date_of_purchase', 'total_amount')
    search_fields = ('user__username',)

@admin.register(OrderDetails)
class OrderDetailsAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'quantity', 'price')
    search_fields = ('order__id', 'product__name')

@admin.register(Receipt)
class ReceiptAdmin(admin.ModelAdmin):
    list_display = ('order', 'number_of_items')
    search_fields = ('order__id',)
