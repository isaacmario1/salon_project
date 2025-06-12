# Create your views here.
from django.shortcuts import render

def home(request):
    return render(request, 'core/home.html')

def services(request):
    return render(request, 'core/services.html')

def booking(request):
    return render(request, 'core/booking.html')

def contact(request):
    return render(request, 'core/contact.html')

def gallery(request):
    return render(request, 'core/gallery.html')

def about(request):
    return render(request, 'core/about.html')

def testimonials(request):
    return render(request, 'core/testimonials.html')
