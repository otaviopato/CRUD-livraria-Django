from django.urls import path, include
from .views import novo_autor

urlpatterns = [
    path('', novo_autor),
]
