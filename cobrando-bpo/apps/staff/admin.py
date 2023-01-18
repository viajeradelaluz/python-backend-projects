from django.contrib import admin

from .models import Departamento, Empleado

admin.site.register((Empleado, Departamento))
