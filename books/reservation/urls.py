from django.conf.urls import url
from reservation import views

urlpatterns = [
    url(r'^$', views.reservationPageView.as_view(), name='index'),
]
