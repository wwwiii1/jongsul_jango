from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from reservation.models import Hospital, Reservation
from django import forms
from django.contrib.auth.models import User
# Create your views here.
class reservationPageView(TemplateView):
    def get(self, request, *args, **kwargs):
        form = ReservationForm()
        return render(request, 'reservation/index.html',{'form':form})

    def post(self, request, *args, **kwargs):
        #reservation 추가
        req = request.session['user_id']
        user2 = User.objects.get(username=req)

        reservation_date = request.POST['reservation_date']
        hospital = request.POST['hospital']

        reservation = Reservation(username_id=user2,reservation_date=reservation_date,hospital=hospital)
        reservation.save()

        return redirect('reservation_result/')

class reservationResultPageView(TemplateView):
    def get(self, request, *args, **kwargs):
        try:
            req = request.session['user_id']
            reservation_all = Reservation.objects.all()#filter(username_id=req)
            reservation_bind = {'reservation_all': reservation_all}
            return render(request, 'reservation/reservation_result.html', reservation_bind)
        except:
            return redirect('home')

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['reservation_date','hospital']
