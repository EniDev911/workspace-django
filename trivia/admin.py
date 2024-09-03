from django.contrib import admin
from .models import Categoria

# Requerimiento
# ●	El superusuario debe poder crear las categorías usando DjangoAdmin..
admin.site.register(Categoria)