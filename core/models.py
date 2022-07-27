from ast import Pass
from django.db import models

# Create your models here.

class Post(models.Model):
    title=models.CharField(verbose_name='Titulo', max_length=250)
    content=models.TextField(verbose_name='Contenido')

    def __str__(self):
        return "%s %s" % (self.title, self.content)
# ------------------------------------------------------------------------------    
class Clase(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion= models.TextField()
    
    
    def __str__(self):
        return "%s %s" % (self.nombre, self.descripcion)
    
# ------------------------------------------------------------------------------    
class Estudiante(models.Model):
    nombre = models.CharField(max_length=50)
    apellidos= models.TextField()    
    
    def __str__(self):
        return "%s %s" % (self.nombre, self.apellidos)
    
# ------------------------------------------------------------------------------    
class Matricula(models.Model):
    clases = models.ForeignKey(Clase,on_delete=models.PROTECT)
    estudiantes= models.ForeignKey(Estudiante,on_delete=models.PROTECT)
    notas=models.FloatField()    
    def __str__(self):
        return "%s %s %s" % (self.clases, self.estudiantes,self.notas) 

