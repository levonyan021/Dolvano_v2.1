from cart.models import Cart


def get_cart_items(request):

    if request.user.is_authenticated:
        user = request.user
        cart_items, created = Cart.objects.get_or_create(user=user, completed=False)
        items = cart_items.cartitemlist_set.all()
        total_cart_items = cart_items.get_cart_total_quantity
    else:
        items = []
        cart_items = {'get_cart_total_quantity': 0, 'get_cart_total_price': 0}
        total_cart_items = cart_items['get_cart_total_quantity']
    context = {'items': items, 'cart_items': cart_items, 'total_cart_items': total_cart_items}
    return context


def cart_item_counts(request):

    if request.user.is_authenticated:
        user = request.user
        cart_items, created = Cart.objects.get_or_create(user=user, completed=False)
        total_cart_items = cart_items.get_cart_total_quantity
    else:
        cart_items = {'get_cart_total_quantity': 0, 'get_cart_total_price': 0}
        total_cart_items = cart_items['get_cart_total_quantity']
    context = {'total_cart_items': total_cart_items}
    return context
