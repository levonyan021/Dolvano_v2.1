from django.contrib import admin

from .models import Cart, CartItemList


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    pass


@admin.register(CartItemList)
class CartItems(admin.ModelAdmin):
    pass
