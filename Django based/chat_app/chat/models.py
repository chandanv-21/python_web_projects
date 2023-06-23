from django.db import models
from datetime import datetime

# Create your models here.

class Room(models.Model):
    roomName=models.CharField(max_length=1000)

    def __str__(self) :
        return self.roomName
    
class Message(models.Model):
    msg=models.CharField(max_length=1000000)
    dates= models.DateTimeField(default=datetime.now, blank=True)
    user=models.CharField(max_length=10000)
    room=models.CharField(max_length=10000)

