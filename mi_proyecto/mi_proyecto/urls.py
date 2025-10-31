from django.contrib import admin
from django.urls import path , include

urlpatterns = [
    path('', include('productos.urls')),
    path('admin/', admin.site.urls),
]