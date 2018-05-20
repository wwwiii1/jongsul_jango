from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.template import RequestContext

class LoginPageView(TemplateView):
    template_name = 'usermanage/login.html'

    def get_context_data(self, **kwargs):
        context = super(LoginPageView, self).get_context_data(**kwargs)
        return context

class SigninPageView(TemplateView):
    template_name = 'usermanage/signin.html'

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','password']

def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(**form.cleaned_data)
            login(request, new_user)
            return redirect('home')
    else:
        form = UserForm()
        return render(request,'usermanage/signin.html',{'form':form})

def signin(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        username=request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse('로그인 실패, 다시 시도해 보세요')

    else:
        form = LoginForm()
        return render(request,'usermanage/login.html',{'form':form})
