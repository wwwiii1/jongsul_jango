from django.conf.urls import url
from usermanage import views

urlpatterns = [
    url(r'^$', views.LoginPageView.as_view(), name='login'),
    url(r'^signin/$', views.signin, name='signin'),
    url(r'^signin/join/$',views.signup, name='join'),
]
