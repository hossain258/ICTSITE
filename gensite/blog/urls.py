from django.urls import path
from blog import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('services/', views.services, name='services'),
    path('client/', views.client, name='client'),
    path('portfolio/', views.portfolio, name='portfolio'),
]

