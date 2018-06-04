from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserLog(models.Model):
    username = models.CharField(max_length=100)
    atopy_true = models.IntegerField()
    log_date = models.DateTimeField(auto_now_add = True)


