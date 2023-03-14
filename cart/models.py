from django.contrib.auth.models import User
from django.db import models

from main.models import Product


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return str(self.id)

    @property
    def get_total_cart_price(self):
        product_items = self.cartitemlist_set.all()
        total_price = sum([product.get_product_total_price for product in product_items])
        return total_price

    @property
    def get_cart_total_quantity(self):
        items = self.cartitemlist_set.all()
        total_items = sum([product.quantity for product in items])
        return total_items


class CartItemList(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey('Cart', on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_product_total_price(self):
        total_items_price = self.product.price * self.quantity
        return total_items_price

    def __str__(self):
        return self.product.name
