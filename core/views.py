from django.shortcuts import render,redirect,get_object_or_404,redirect
from django.views.generic import View


#! traemos la clase de froms.py PostCreateForm
from .forms import PostCreateForm
from .models import Post

#! importamos de django
from django.urls import reverse_lazy



class HomeView(View):
    def get(self,request, *args, **kwargs):
        context={
            
        }
        return render(request,'core/home.html',context)
# ------------------------------------------------------------------------------------------------------    
    
class AboutView(View):
    def get(self,request, *args, **kwargs):
        context={
            
        }
        return render(request,'core/about.html',context)
# ------------------------------------------------------------------------------------------------------  
class ProjectView(View):
    def get(self,request, *args, **kwargs):
        context={
            
        }
        return render(request,'core/project.html',context)
    
# ------------------------------------------------------------------------------------------------------  
class ContactView(View):
    def get(self,request, *args, **kwargs):
        context={
            
        }
        return render(request,'core/contact.html',context)
    
# ------------------------------------------------------------------------------------------------------  

class ProjectUnoView(View):
    
    def get(self,request,*args, **kwargs):
        form=PostCreateForm() #?pasamos la clase form de traida de forms.py a una variable llamada form
        context={
            'form':form
        }
        return render(request,'core/proyecto1.html',context)
    
    #todo el get los cambiamos a post dentro de la misma clase
    def post(self,request,*args, **kwargs):
        
        if request.method == "POST": #?si el metodo es post
            form=PostCreateForm(request.POST) #? traeme el formulario y toda la info que esta dentro de post(request.POST) en el formulario en la pagina create
            
            if form.is_valid(): #? si el formulario es valido obtenemos el titulo y el contenido la info que ingresamos en la pagina create
                title = form.cleaned_data.get('title') #? aqui obtenemos lo que ingresamos en el campo title del formulario
                content = form.cleaned_data.get('content') #? aqui obtenemos lo que ingresamos en el campo content del formulario
                
                
                p,created = Post.objects.get_or_create(title=title, content=content) #? Al modelo Post (BBDD) le asiganamos lo que tenemos en el formulario
                p.save() #? guardamos la informacion en el modelo de la BBDD
                return redirect('core:home') #? lo redireccionamos al home
            
        context={
            
        }
        return render(request,'core/projecto1.html',context)
    
# ------------------------------------------------------------------------------------------------------     
    
    

    