from django.shortcuts import render, redirect
from .models import Appointment, Service
from .forms import AppointmentForm

def book_service(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('booking-success')
    else:
        form = AppointmentForm()
    return render(request, 'bookings/book.html', {'form': form})


def home(request):
    return render(request, 'bookings/home.html')

def success(request):
    return render(request, 'bookings/success.html')