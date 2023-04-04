from django.contrib import admin
from .models import Visitante, Paciente, Habitacion, Piso
# Register your models here.

admin.site.register(Visitante)
admin.site.register(Paciente)
admin.site.register(Habitacion)
admin.site.register(Piso)