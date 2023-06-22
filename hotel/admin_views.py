from django.shortcuts import render, redirect, get_object_or_404
from .forms import CreateUserForm, EditUserForm
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Room, RoomType
from reservation.models import Reservation, ServiceReservation
from datetime import date

def home(request):
    guests= User.objects.exclude(is_superuser=True).count()
    rooms = Room.objects.count()
    available_rooms = Room.objects.filter(is_available=True).count()
    unavailable_rooms = Room.objects.filter(is_available=False).count()
    single_rooms = Room.objects.filter(room_type=1).count()
    double_rooms = Room.objects.filter(room_type=2).count()
    triple_rooms = Room.objects.filter(room_type=3).count()
    deluxe_rooms = Room.objects.filter(room_type=4).count()
    executive_suite = Room.objects.filter(room_type=5).count()
    presidential_suite = Room.objects.filter(room_type=6).count()

    context = {
        'guests': guests,
        'rooms': rooms,
        'available_rooms': available_rooms,
        'unavailable_rooms': unavailable_rooms,
        'single_rooms': single_rooms,
        'double_rooms': double_rooms,
        'triple_rooms': triple_rooms,
        'deluxe_rooms': deluxe_rooms,
        'executive_suite': executive_suite,
        'presidential_suite': presidential_suite,
    }
    return render(request, 'administrator/dashboard.html', context)


def base(request):
    return render(request, 'administrator/base.html')


def guest(request):
    users = User.objects.all()
    return render(request, 'administrator/guest.html', {'users':users})


def add_guest(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_guest')
    else:
        form = CreateUserForm()
    return render(request, 'administrator/add_guest.html', {'form': form})


def edit_guest(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        form = EditUserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('admin_guest')
    else:
        form = EditUserForm(instance=user)
    return render(request, 'administrator/edit_guest.html', {'form': form, 'user': user})


def delete_guest(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        user.delete()
        return redirect('admin_guest')


def room(request):
    rooms = Room.objects.all()
    reservations = Reservation.objects.all()
            
    return render(request, 'administrator/rooms.html', {'rooms': rooms})


def reservation(request):
    rooms = Room.objects.all()
    reservations = Reservation.objects.all()
    
    return render(request, 'administrator/reservations.html', {'reservations': reservations})


def service(request):
    services = ServiceReservation.objects.all()

    return render(request, 'administrator/services.html', {'services': services})