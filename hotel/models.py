from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class RoomType(models.Model):
    type_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=2000)
    price = models.IntegerField()
    image = models.ImageField(upload_to='images')  
  
    def __str__(self):  
        return self.name

class Room(models.Model):
    room_id = models.IntegerField(default=True, primary_key=True)
    room_number = models.CharField(max_length=10)
    room_type = models.ForeignKey(RoomType, on_delete=models.CASCADE)
    is_available = models.BooleanField(default=True)
    is_occupied = models.BooleanField(default=False)

    def __str__(self):  
        return f"{self.room_number} -----: {self.room_type.name}"
    
class Service(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=2000)
    price = models.IntegerField()
    image = models.ImageField(upload_to='images')  
  
    def __str__(self):  
        return self.name
    
