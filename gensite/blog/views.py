from django.shortcuts import render
from.models import aboutus

# Create your views here.

def home(request):
    obj = aboutus.objects.all()[0]
    diction = {
        
        'object':obj,
        'Title': 'Home'
        
    }
    return render(request, 'home.html', context=diction)

def about(request):
    obj = aboutus.objects.all()[0]
    diction = {
        'object':obj,
        'Title': 'About'
    }
    return render(request, 'about.html', context=diction)

def contact(request):
    diction = {
        
        'Title': 'Contact'
    }
    return render(request, 'contact.html', context=diction)

def services(request):
    diction = {
        'Title':'services'
    }
    return render(request, 'services.html', context=diction)

def client(request):
    diction = {
        'Title':'client'
    }
    return render(request, 'client.html', context=diction)

def portfolio(request):
    diction = {
        'Title':'portfolio'
    }
    return render(request, 'portfolio.html', context=diction)
