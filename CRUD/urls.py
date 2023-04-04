from django.urls import path
from .views import VisitantesView, PacientesView, HabitacionesView, PisosView

urlpatterns = [
    path('pisos/', PisosView.as_view(), name='pisos_list'),
    path('pisos/<int:id>', PisosView.as_view(), name='pisos_process'),
    path('habitaciones/', HabitacionesView.as_view(), name='habitaciones_list'),
    path('habitaciones/<int:id>', HabitacionesView.as_view(), name='habitaciones_process'),
    path('pacientes/', PacientesView.as_view(), name='pacientes_list'),
    path('pacientes/<int:id>', PacientesView.as_view(), name='pacientes_process'),
    path('visitantes/', VisitantesView.as_view(), name='visitantes_list'),
    path('visitantes/<int:id>', VisitantesView.as_view(), name='visitantes_process'),
]