from django.template.defaulttags import url
from django.urls import path, include
from .views import *

app_name = 'main'
urlpatterns = [
    path('', index, name='index'),

    path('ShowClocks/', wallclocks_list, name='wallclocks_list'),

    path('Decorations/', decoration_list, name='decorations_link'),

    path('Fireplace/', fireplace_list, name='fireplace_list'),

    path('Dolvano_home/', dolvano_home_list, name='dolvano_home_list'),

    path('Special_Orders/', special_orders_list, name='special_orders_list'),

    path('Info/', information, name='information'),

    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),

    path('live-search/', live_search, name='live_search'),

    path('Product/<int:product_pk>', product_page, name='product_page'),


]
