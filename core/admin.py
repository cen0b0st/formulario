from django.contrib import admin

from .models import Post,Estudiante,Matricula,Clase

from .models import Matricula,Post, Estudiante,Clase

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display=('title','content')

@admin.register(Estudiante)
class EstudianteAdmin(admin.ModelAdmin):
    list_display=('nombre','apellidos')


@admin.register(Matricula)
class MatriculaAdmin(admin.ModelAdmin):
    list_display= ('clases','estudiantes','notas')
    
    
    
@admin.register(Clase)
class ClaseAdmin(admin.ModelAdmin):
    list_display=('nombre','descripcion')