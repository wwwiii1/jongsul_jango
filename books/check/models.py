from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    apoti_true = models.IntegerField()
    log_date = models.DateTimeField()


