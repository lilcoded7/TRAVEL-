from django.shortcuts import render
from .models import Register

# Create your views here.





def home(request):
    
    return render(request, 'TOUR/home.html')

def contact(request):
    return render(request, 'TOUR/contact.html')

def about(request):

    return render(request, 'TOUR/about.html')

def service(request):

    return render(request, 'TOUR/services.html')

def register(request):

    if request.method == 'POST':
        name     = request.POST['name']
        email    = request.POST['email']
        phone    = request.POST['phone']
        password = request.POST['name']

        user = Register.objects.create(name=name,email=email,phone=phone,password=password)
        



    return render(request, 'TOUR/register.html')