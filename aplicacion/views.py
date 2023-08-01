from django.shortcuts import render
from django.http import HttpResponse
from aplicacion.models import *
from .forms import * 
# Create your views here.
def index(request):
    return render(request, "aplicacion/base.html")

def Medicos(request):
    ctx = {"Medicos": medico.objects.all}
    return render(request, "aplicacion/Medicos.html", ctx)

def Pediatras(request):
    ctx = {"Pediatras": pediatra.objects.all}
    return render(request, "aplicacion/Pediatras.html",ctx)

def Odontologos(request):
    ctx = {"Odontologos": odontologo.objects.all}
    return render(request, "aplicacion/Odontologos.html",ctx)

def Fonoaudiologo(request):
    ctx = {"Fonoaudiologos": fonoaudiologo.objects.all}
    return render(request, "aplicacion/Fonoaudiologos.html", ctx)
#_______________crear profesionales_______________________
def NuevoProfesional(request):
    ctx = {"NuevoProfesionales": Nuevoprofesional.objects.all}
    return render(request, "aplicacion/NuevoProfesionales.html", ctx)

def profesionalForm(request):
    if request.method=="POST":
        NuevoProfesionales = Nuevoprofesional(nombre=request.POST['nombre'], apellido=request.POST['apellido'], email=request.POST['email'],profesion=request.POST['profesion'])
        NuevoProfesionales.save()
        return HttpResponse("se registro exitosamente")
        
    return render(request,"aplicacion/profesionalForm.html")

#_____________________buscar________________________
def buscarMedicos(request):
    return render(request,"aplicacion/buscarMedicos.html")

def buscar2(request):
    if request.GET['apellidos']:
        apellido =request.GET['apellidos']
        Fonoaudiologo = fonoaudiologo.objects.filter(apellido__icontains=apellido)
        Odontologo = odontologo.objects.filter(apellido__icontains=apellido)
        Pediatra = pediatra.objects.filter(apellido__icontains=apellido)
        Medico= medico.objects.filter(apellido__icontains=apellido)
        return render(request,"aplicacion/resultadosBusqueda.html",
                      {"apellido": apellido, "Fonoaudiologo":Fonoaudiologo, "Odontologo":Odontologo, "Pediatra":Pediatra, "Medico":Medico})
    return HttpResponse("no se ingresaron los datos correspondientes")