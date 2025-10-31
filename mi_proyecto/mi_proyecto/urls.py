from django.contrib import admin
from django.urls import path, include
from productos import views

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('productos/', include('productos.urls')),
]