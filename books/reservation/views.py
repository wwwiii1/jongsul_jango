from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from reservation.models import Hospital, Reservation
from django import forms
# Create your views here.
class reservationPageView(TemplateView):
    def get(self, request, *args, **kwargs):
        form = ReservationForm()
        return render(request, 'reservation/index.html',{'form':form})

    def post(self, request, *args, **kwargs):
        #reservation 추가

        user = request.POST['user']
        reservation_date = request.POST['reservation_date']
        hospital = request.POST['hospital']

        reservation = Reservation(user=user,reservation_date=reservation_date,hospital=hospital)
        reservation.save()

        return redirect('reservation/')

class reservationResultPageView(TemplateView):
    def get(self, request, *args, **kwargs):
        try:
            reservation_all = Reservation.objects.all()
            reservation_bind = {'reservation_all': reservation_all}
            return render(request, 'reservation/reservation_result.html', reservation_bind)
        except:
            return redirect('reservation/')

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['user','reservation_date','hospital']
