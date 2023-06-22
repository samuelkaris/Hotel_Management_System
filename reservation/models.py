from django.db import models
from hotel.models import Room, Service
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import time, datetime
from django.core.exceptions import ValidationError

def start_time():
    now = datetime.now()
    time = now.time()
    start = time.replace(hour=0, minute=0, second=0, microsecond=0)
    return start


def end_time():
    now = datetime.now()
    time = now.time()
    start = time.replace(hour=12, minute=0, second=0, microsecond=0)
    return start

class Reservation(models.Model):
    guest = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    start_date = models.DateField()
    start_time = models.TimeField(default=start_time)
    end_date = models.DateField()
    end_time = models.TimeField(default=end_time)


    def __str__(self):
        return f"Guest: {self.guest.username} - Room: {self.room.room_number} "
    
    @property
    def duration(self):
        return (self.end_date - self.start_date).days
    
    class Meta:
        ordering = ['start_date']

    
    
class ServiceReservation(models.Model):
    guest = models.ForeignKey(User, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    reservation_date = models.DateField()
    reservation_time = models.TimeField()

    def __str__(self):
        return f"Service: {self.service.name} - Guest: {self.guest.username}"
    
    