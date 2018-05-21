from django.conf.urls import url
from reservation import views

urlpatterns = [
    url(r'^$', views.reservationPageView.as_view(), name='index'),
    url(r'^reservation_result/$', views.reservationResultPageView.as_view(), name='reservation_result'),
]
