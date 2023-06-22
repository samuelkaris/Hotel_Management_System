from django.shortcuts import render, redirect
from .models import RoomType, Service
from reservation.models import Reservation
from django.contrib import messages
from datetime import datetime, timedelta, date


def home(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            return redirect('admin_dashboard')
    return render(request, 'guest/home.html')

def base(request):
    return render(request, 'guest/base.html')

def room(request):
    room_types = RoomType.objects.all()
    return render(request, 'guest/room.html', {'room_types': room_types})

def service(request):
    services = Service.objects.all()

    return render(request, 'guest/service.html', {'services': services})

def notify(request):
    
    reservations = Reservation.objects.filter(guest=request.user)
    expiring_reservations = []
    today = date.today()

    for reservation in reservations:
        if today == reservation.end_date:
            messages.warning(request, f'Your reservation for Room {reservation.room.room_number} is about to expire.')
            expiring_reservations.append(reservation)

    request.session['expiring_reservations_count'] = len(expiring_reservations)

    return render(request, 'guest/notify.html')