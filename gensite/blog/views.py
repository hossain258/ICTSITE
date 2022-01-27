from django.shortcuts import render
from.models import aboutus
from.models import contactus

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
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone_Number = request.POST['phone_Number']
        message = request.POST['message']
        values = contactus(name=name, email=email,phone_Number=phone_Number,message=message)        
        values.save()
        return render (request, 'sendmsg.html')
        
    
    
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
