from django.urls import path, include
from aplicacion.views import *

urlpatterns = [
    path('', index, name="inicio"),
#___________________________________________________________________________
    path('Fonoaudiologo/', Fonoaudiologo, name="Fonoaudiologos"),
    path('Medicos/', Medicos, name="Medicos"),
    path('Odontologos/', Odontologos, name="Odontologos"),
    path('Pediatras/', Pediatras, name="Pediatras"),  
#___________________________________________________________________________
    path('NuevoProfesionales/', NuevoProfesional, name="Nuevo_profesional"),
    path('profesional_Form/', profesionalForm, name="profesional_Form"),   
#___________________________________________________________________________
    path('buscar_medicos/', buscarMedicos, name="buscar_medicos"),
    path('buscar2/', buscar2, name="buscar2"),
]