from django.urls import path
from blog import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('services/', views.service, name='service'),
    path('service-details/<int:id>/', views.serviceDetails, name='service-details'),
    path('client/', views.client, name='client'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('privacy/', views.privacy, name='privacy'),
]

