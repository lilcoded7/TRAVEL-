from django.shortcuts import render

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

    return render(request, 'TOUR/register.html')