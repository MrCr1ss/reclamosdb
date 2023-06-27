from django.db import models

# Create your models here.
#Modelo tabla de registro
class Registro (models.Model):
    rut=models.CharField(max_length=11,primary_key=True)
    nombre=models.CharField(max_length=30,verbose_name='Nombre')
    apellido=models.CharField(max_length=30, verbose_name='Apellido')
    fecha=models.DateField()
    descripcion=models.CharField(max_length=30,verbose_name='Descripción')
    mensaje=models.CharField(max_length=200, verbose_name='Mensaje')