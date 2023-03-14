from django.template.defaulttags import url
from django.urls import path
from .views import cart, update_cart

urlpatterns = [
    path('cart/', cart, name='cart'),
    path('update_cart/', update_cart, name='update_cart'),
    # url(r'^cart/$', cart),

]
