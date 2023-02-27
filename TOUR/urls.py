from django.urls import path 
from . import views 


urlpatterns = [
    
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('register', views.register, name='register'),
    path('services', views.service, name='services'),
    path('contact', views.contact, name='contact')

]