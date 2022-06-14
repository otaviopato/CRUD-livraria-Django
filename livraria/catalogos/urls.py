from django.urls import path, include
from .views import catalogo_create
from .views import catalogo_list

urlpatterns = [
    path('', catalogo_create),
    path('', catalogo_list)
]
