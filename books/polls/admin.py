from django.contrib import admin
from reservation.models import Reservation
from check.models import UserLog
# Register your models here.

admin.site.register(Reservation)
admin.site.register(UserLog)
