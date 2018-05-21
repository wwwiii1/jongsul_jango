from django.conf.urls import url
from check import views

urlpatterns = [
    url(r'^$', views.checkPageView.as_view(), name='check'),
    url(r'checkresult/$',views.checkResultPageView.as_view(), name='check_result'),
]
