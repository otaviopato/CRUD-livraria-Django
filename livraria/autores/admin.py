from django.contrib import admin

# Register your models here.
from .models import Autor, AutorLivro
# Register your models here.

admin.site.register(Autor)
admin.site.register(AutorLivro)
