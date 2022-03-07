from re import template
from django.http import HttpResponse
from django.shortcuts import render 
from.models import aboutus
from.models import contactus
from.models import services
from.models import clientdata
from.models import Portfolio
from.models import Dynamicslider
from.models import Gallery
from django.views.generic.list import ListView


# Create your views here.

def home(request):
    # qs  = services.objects.all()
    obj = aboutus.objects.all()[0]
    # qs = aboutus.objects.all()
    qs = services.objects.all()
    cdata = clientdata.objects.all()
    sliderdata =Dynamicslider.objects.all()
   
   
    diction = {
        
        'object':obj,
        'Title': 'Home',
        'qs':qs,
        'cdata':cdata,
        'sliderdata':sliderdata,
        
        
    }
    return render(request, 'home.html', context=diction)

def about(request):
    # img1=("http://127.0.0.1:8000/static/assets/images/more-info.jpg","http://127.0.0.1:8000/static/assets/images/service_01.jpg","http://127.0.0.1:8000/static/assets/images/service_03.jpg")
    
    obj = aboutus.objects.all()[0]
    diction = {
        'object':obj,
        'Title': 'About',
        
        
    }
    return render(request, 'about.html', context=diction)

def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone_Number = request.POST.get('phone_Number')
        message = request.POST['message']
        values = contactus(name=name, email=email,phone_Number=phone_Number,message=message)        
        values.save()
        return render (request, 'sendmsg.html')
        
    
    
    diction = {
        
        'Title': 'Contact'
     }
    return render(request, 'contact.html', context=diction)

# def service(request):
#     qs = services.objects.all()
#     diction = {
#         'Title':'services',
#         'qs':qs
#     }
#     return render(request, 'services.html', context=diction)



class ServiceListView(ListView):

    model = services
    template_name = 'services.html'
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['qs'] = services.objects.all()
        context['Title'] = 'Services'
        return context








def serviceDetails(request, id):
    servicedata = services.objects.get(id=id)
    
    diction = {
        'Title':'services details',
        'servicedata':servicedata
    }
    return render(request, 'service_details.html', context=diction)
    
    
    
# def client(request):
#     cdata = clientdata.objects.all()
#     diction = {
#         'Title':'Client',
#         'cdata':cdata
#     }
#     return render(request, 'client.html', context=diction)

class ClientListView(ListView):
    
    model = clientdata
    template_name = 'client.html'
    paginate_by = 1
    context_object_name ='cdata'
    
    # def get_queryset(self):
    #     return clientdata.objects.all()
    
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cdata'] = clientdata.objects.all()
        context['Title'] = 'Client'
        return context

def portfolio(request):
    portfdata= Portfolio.objects.all()
    diction = {
        'Title':'Portfolio',
        'portfdata':portfdata
    }
    return render(request, 'portfolio.html', context=diction)

def privacy(request):
    diction = {
        'Title': 'Privacy Policy'
    }
    return render(request, 'privacy.html', context=diction)



def gallery(request):
    galrdata= Gallery.objects.all()
    diction = {
        'Title':'Gallery',
        'galrdata':galrdata
    }
    return render(request, 'Gallery.html', context=diction)



