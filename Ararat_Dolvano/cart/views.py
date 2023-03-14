from django.shortcuts import render
from django.http import JsonResponse
import json

from main.models import Product
from .models import Cart, CartItemList
from .services import get_cart_items


def cart(request):
    total_cart_items = 0

    context = get_cart_items(request)
    if context['total_cart_items'] != 0:
        return render(request, 'main/cart.html', context)
    else:
        return render(request, 'main/empty_cart.html')


def update_cart(request):
    data = json.loads(request.body)

    product_id = data['productId']
    action = data['action']

    user = request.user
    product = Product.objects.get(id=product_id)
    cart_items, created = Cart.objects.get_or_create(user_id=user.id, completed=False)

    cart_item, created = CartItemList.objects.get_or_create(cart=cart_items, product=product)

    print(action)
    if action == 'add':
        cart_item.quantity = cart_item.quantity + 1
    elif action == 'remove':
        if cart_item.quantity <= 0:
            cart_item.quantity = cart_item.quantity
        else:
            cart_item.quantity = cart_item.quantity - 1

    cart_item.save()

    if cart_item.quantity == 0:
        cart_item.delete()

    return JsonResponse('Item was added', safe=False)
