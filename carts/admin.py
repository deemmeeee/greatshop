from django.contrib import admin
from .models import Cart, CartItem
# Register your models here.

# we create these classes for showing up 
# cart items and carts with all parametrs that we choose
class CartAdmin(admin.ModelAdmin):
    list_display = ('cart_id', 'date_added')

class CartItemAdmin(admin.ModelAdmin):
    list_display = ('product', 'cart', 'quantity', 'is_active')

admin.site.register(Cart, CartAdmin)
admin.site.register(CartItem, CartItemAdmin)