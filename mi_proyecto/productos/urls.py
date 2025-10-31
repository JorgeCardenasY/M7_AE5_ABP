from django.urls import path
from . import views

urlpatterns = [
    path('', views.productos_view, name='productos'),
]