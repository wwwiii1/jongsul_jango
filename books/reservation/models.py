from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hospital = models.CharField(max_length=100)
    reservation_date = models.DateField()

    def __unicode__(self):
        return self.user

class Hospital(models.Model):
    name = models.CharField(max_length=100)
    call = models.CharField(max_length=100)
    location = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name
