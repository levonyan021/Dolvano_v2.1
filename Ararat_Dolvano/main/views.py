from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm

from cart.services import cart_item_counts
from .forms import LoginForm
from .models import *
from django.views.generic import ListView
from django.http import JsonResponse
from django.core.paginator import Paginator
import json
import random



def index(request):
    clocks = list(Product.objects.filter(rubric__name='Clock'))
    random_clocks = random.sample(clocks, 2)
    decorations = list(Product.objects.filter(rubric__name='Decoration'))
    random_decorations = random.sample(decorations, 3)
    clocks_new = list(Product.objects.all())
    random_clocks_new = random.sample(clocks_new,2)
    clocks_4_items = random.sample(clocks_new, 4)
    popular_items = Product.objects.filter(popular = True)
    total_cart_items = cart_item_counts(request)['total_cart_items']
    context={
        'navbar': 'index',
        'decorations': random_decorations,
        'clocks': random_clocks,
        'clocks_new': random_clocks_new,
        'clocks_4' : clocks_4_items,
        'populars': popular_items,
        'total_cart_items': total_cart_items
    }
    return render(request, 'main/index.html', context)


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('main:index')
        else:
            error = 'Invalid username or password.'
    else:
        form = LoginForm()
        error = None
    context = {
        'form': form,
        'error': 'Invalid username or password.',
    }
    return render(request, 'main/login.html', context)




def logout_view(request):
    logout(request)
    return redirect('main:index')

# Search worked
def live_search(request):
    total_cart_items = cart_item_counts(request)['total_cart_items']
    query = request.GET.get('q')
    if query:
        products = Product.objects.filter(name__icontains=query)
    else:
        products = Product.objects.none()
    return render(request, 'main/live_search.html', {
            'products': products,
            'query': query,
            'total_cart_items': total_cart_items,
        })




def wallclocks_list(request):
    total_cart_items = cart_item_counts(request)['total_cart_items']
    wallclocks = Product.objects.filter(rubric__name='Clock')
    paginator = Paginator(wallclocks, 5)
    page = request.GET.get('page')
    wallclocks = paginator.get_page(page)
    context = {
        'wallclocks': wallclocks,
        'navbar': 'showClocks',
        'total_cart_items': total_cart_items
    }
    return render(request, 'main/wall_clocks.html', context)


def fireplace_list(request):
    fireplaces = Product.objects.filter(rubric__name='BioFireplace')
    paginator = Paginator(fireplaces, 5)
    page = request.GET.get('page')
    fireplaces = paginator.get_page(page)
    total_cart_items = cart_item_counts(request)['total_cart_items']

    context = {
        'fireplaces': fireplaces,
        'navbar': 'fireplace_list',
        'total_cart_items': total_cart_items,
    }
    return render(request, 'main/bio_fireplace.html', context)


def dolvano_home_list(request):
    dolvano_home = Product.objects.filter(rubric__name='DolvanoHome')
    paginator = Paginator(dolvano_home, 5)
    page = request.GET.get('page')
    dolvano_home = paginator.get_page(page)
    total_cart_items = cart_item_counts(request)['total_cart_items']
    context = {
        'dolvano_home': dolvano_home,
        'navbar': 'dolvano_home_list',
        'total_cart_items': total_cart_items
    }
    return render(request, 'main/dolvano_home.html', context)


def special_orders_list(request):
    special_orders = Product.objects.filter(rubric__name='SpecialOrders')
    paginator = Paginator(special_orders, 5)
    page = request.GET.get('page')
    special_orders = paginator.get_page(page)
    total_cart_items = cart_item_counts(request)['total_cart_items']

    context = {
        'special_orders': special_orders,
        'navbar': 'special_orders_list',
        'total_cart_items': total_cart_items,
    }
    return render(request, 'main/special_orders.html', context)

def information(requset):
    information = Information.objects.all()
    total_cart_items = cart_item_counts(requset)['total_cart_items']

    context = {
        'navbar': 'information',
        'information': information,
        'total_cart_items': total_cart_items,
    }
    return render(requset, 'main/information.html', context)


# Don't finish
def decoration_list(request):
    decorations = Product.objects.filter(rubric__name='Decoration')
    paginator = Paginator(decorations, 5)
    page = request.GET.get('page')
    decorations = paginator.get_page(page)
    total_cart_items = cart_item_counts(request)['total_cart_items']

    context = {
        'decorations': decorations,
        'navbar': 'decorations_link',
        'total_cart_items': total_cart_items,

    }
    return render(request, 'main/decorations.html', context)


def product_page(request, product_pk):
    product = Product.objects.get(pk=product_pk)
    return render(request, 'main/one_product_page.html',
    {
        'product': product
    }
    )







