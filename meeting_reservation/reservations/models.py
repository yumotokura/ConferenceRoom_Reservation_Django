from django.db import models
from django.utils import timezone

class Room(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Reservation(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    reserved_by = models.CharField(max_length=100)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return f'{self.room.name} reserved by {self.reserved_by} from {self.start_time} to {self.end_time}'

    def is_conflicting(self, start_time, end_time):
        return self.start_time < end_time and self.end_time > start_time
