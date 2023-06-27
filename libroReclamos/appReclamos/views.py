from django.shortcuts import render
from . import forms
from appReclamos.models import Registro

# Create your views here.

def listadoRegistro(request):
    registros=Registro.objects.all()
    data={'registros':registros}
    return render(request,'listado.html',data)

def index(request):
    form=forms.RegistroReclamo()
    if request.method=='POST':
        form=forms.RegistroReclamo(request.POST)
        if form.is_valid():
            form.save()
            return listadoRegistro(request)
    data={'form':form}
    return render(request,'index.html',data)