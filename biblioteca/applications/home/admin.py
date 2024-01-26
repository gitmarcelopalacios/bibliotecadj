from django.contrib import admin

# Register your models here.
from.models import Persona, Empleados, Cliente

admin.site.register(Persona)
admin.site.register(Empleados)
admin.site.register(Cliente)