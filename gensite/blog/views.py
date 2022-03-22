from re import template
from django.http import HttpResponse
from django.shortcuts import render 
from.models import Team, aboutus
from.models import contactus
from.models import services
from.models import clientdata
from.models import Portfolio
from.models import Dynamicslider
from.models import Gallery
from.models import Team
from django.views.generic.list import ListView
from django.core.paginator import Paginator
from django.core.mail import EmailMessage, message
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from gensite.settings import EMAIL_HOST_USER


# Create your views here.


    

def home(request):
    # service_list  = services.objects.all()
    sliderdata =Dynamicslider.objects.all()
    obj = aboutus.objects.all()[0]
    # service_list = aboutus.objects.all()
    # service_list = services.objects.all()[:5]
    service_list = services.objects.filter(is_featured=True)
    
    # paginator = Paginator(service_list, 6)
    # page = request.GET.get('service_Home_page')
    # try:
    #     service_list = paginator.page(page)
    # except PageNotAnInteger:
    #     service_list = paginator.page(1)
    # except EmptyPage:
    #     service_list = paginator.page(paginator.num_pages)

    
    client_list = clientdata.objects.filter(is_featured=True)
    # paginator = Paginator(client_list, 4)
    # page = request.GET.get('client_Home_page')
    # try:
    #     client_list = paginator.page(page)
    # except PageNotAnInteger:
    #     client_list = paginator.page(1)
    # except EmptyPage:
    #     client_list = paginator.page(paginator.num_pages)
    
   
   
    diction = {
        
        'object':obj,
        'Title': 'Home',
        'service_list':service_list,
        'client_list':client_list,
        'sliderdata':sliderdata,
        
        
    }
    return render(request, 'home.html', context=diction)

def about(request):
   
    
    obj = aboutus.objects.all()[0]
    service_list = services.objects.all()
    diction = {
        'object':obj,
        'Title': 'About',
        'service_list':service_list,
        
        
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
        send_email = EmailMessage(
            f"""  message from ICTINEX """,
            f"""Sender:{name}""",
            # from
            f'{EMAIL_HOST_USER}',
            # to
            [email],
            reply_to=[email],
            )
        send_email.send()
        return render (request, 'sendmsg.html')
        
        
    
    service_list = services.objects.all() 
    
    diction = {
        
        'Title': 'Contact',
        'service_list': service_list
    
     }
    return render(request, 'contact.html', context=diction)

# def service(request):
#     service_list = services.objects.all()
#     diction = {
#         'Title':'services',
#         'service_list':service_list
#     }
#     return render(request, 'services.html', context=diction)



class ServiceListView(ListView):

    model = services
    template_name ='services.html'
    paginate_by = 6
    context_object_name ='service_list'
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['service_list'] = services.objects.all()
        context['Title'] = 'Services'
        return context








def serviceDetails(request, id):
    servicedata = services.objects.get(id=id)
    service_list = services.objects.all()
    
    diction = {
        'Title':'services details',
        'servicedata':servicedata,
        'service_list':service_list,
    }
    return render(request, 'service_details.html', context=diction)
    
    
    
# def client(request):
#     cdata = clientdata.objects.all()
#     diction = {
#         'Title':'Client',
#         'cdata':cdata
#     }
#     return render(request, 'client.html', context=diction)







# def clientsss(request):
#     client_list = clientdata.objects.all()
#     page = request.GET.get('page', 1)

#     paginator = Paginator(client_list, 4)
#     try:
#         clients = paginator.page(page)
#     except PageNotAnInteger:
#         clients = paginator.page(1)
#     except EmptyPage:
#         clients= paginator.page(paginator.num_pages)
    
#     context ={
        
#     }
#     context["clients"]=clients

#     return context

# def client(request):
#     client_list = clientdata.objects.all()
#     paginator = Paginator(client_list, 4)

#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#     diction = {
#         'Title':'Client',
#         'page_obj':page_obj,
#     }
#     return render(request, 'client.html', context=diction)











class ClientListView(ListView):
    
    model = clientdata
    template_name = 'client.html'
    paginate_by = 12
    ordering = ['title']
    context_object_name ='client_list'  
    
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['client_list'] = clientdata.objects.all()
        context ['service_list'] = services.objects.all()
        context['Title'] = 'Client'
        return context

def portfolio(request):
    portfdata= Portfolio.objects.all()
    service_list = services.objects.all()
    diction = {
        'Title':'Portfolio',
        'portfdata':portfdata,
        'service_list':service_list,
    }
    return render(request, 'portfolio.html', context=diction)


def portfolioDetails(request, id):
    portfoliodata = Portfolio.objects.get(id=id) 
    service_list = services.objects.all()  
    diction ={
        'Title':'Portfolio details',
        'portfoliodata':portfoliodata,
        'service_list':service_list,
    }
    return render(request, 'portfolio_details.html', context=diction)


def privacy(request):
    
    diction = {
        'Title': 'Privacy Policy'
        
    }
    return render(request, 'privacy.html', context=diction)



def gallery(request):
    galrdata= Gallery.objects.all()
    service_list = services.objects.all()
    diction = {
        'Title':'Gallery',
        'galrdata':galrdata,
        'service_list':service_list,
        
    }
    return render(request, 'Gallery.html', context=diction)


def team(request):
    tmdata= Team.objects.all()
    service_list = services.objects.all()
    diction = {
        'Title':'Team',
        'tmdata':tmdata,
        'service_list':service_list,
    }
    return render(request, 'team.html', context=diction)



