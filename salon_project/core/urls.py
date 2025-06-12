from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('services/', views.services, name='services'),
    path('booking/', views.booking, name='booking'),
    path('contact/', views.contact, name='contact'),
    path('gallery/', views.gallery, name='gallery'),
    path('about/', views.about, name='about'),
    path('testimonials/', views.testimonials, name='testimonials'),
]
