from django import forms
from appReclamos.models import Registro
from datetime import date


#Registro

class RegistroReclamo(forms.ModelForm):
    class Meta:
        model=Registro
        fields='__all__'
    TIPO=(
        ('reclamo', 'Reclamo'),
        ('felicitacion', 'Felicitación'),
    )
    nombre=forms.CharField()
    apellido=forms.CharField()  
    fecha=forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    descripcion=forms.CharField(widget=forms.Select(choices=TIPO))
    mensaje=forms.CharField()



    nombre.widget.attrs['class']='form-control'
    apellido.widget.attrs['class']='form-control'
    fecha.widget.attrs['class']='form-control datetimepicker-input'
    descripcion.widget.attrs['class']='form-control'
    mensaje.widget.attrs['class']='form-control'