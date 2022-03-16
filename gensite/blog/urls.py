from django.urls import path
from blog import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('services/', views.ServiceListView.as_view(), name='service'),
    path('service-details/<int:id>/', views.serviceDetails, name='service-details'),
    path('client/', views.ClientListView.as_view(), name='client'),
    # path('client/', views.client, name='client'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('portfolio_details/<int:id>/', views.portfolioDetails, name='portfolio-details'),
    path('gallery/', views.gallery, name='gallery'),
    path('privacy/', views.privacy, name='privacy'),
    path('team/', views.team, name='team'),
]

