from django.urls import path,include

from .views import ContactView, HomeView,AboutView, ProjectView,ProjectUnoView


app_name='core'

urlpatterns = [
    path('',HomeView.as_view(),name='home'),
    path('about/',AboutView.as_view(),name='about'),
    path('project/',ProjectView.as_view(),name='project'),
    path('contact/',ContactView.as_view(),name='contact'),
    
    path('uno/',ProjectUnoView.as_view(),name='uno'),
    
    
]
