from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('book/', views.book_service, name='book'),
    path('success/', views.success, name='booking-success'),
]
