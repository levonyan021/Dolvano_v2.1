from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('', views.home, name='index'),
    path('acc/signup/', views.signup, name='signup'),
    path('acc/activate/', views.activate, name='activate'),
]
