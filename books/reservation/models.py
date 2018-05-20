from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reservation_date = models.DateField()

    def __unicode__(self):
        return self.user
