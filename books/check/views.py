from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView

# Create your views here.
class checkPageView(TemplateView):
    template_name = 'check/check.html'

    def get_context_data(self, **kwargs):
        context = super(checkPageView, self).get_context_data(**kwargs)
        return context

    def post(self, request, *args, **kwargs):
        #판단 알고리즘..
        return render(request,'check/check_result.html')


class checkResultPageView(TemplateView):
    def get(self, request, *args, **kwargs):
        return render(request, 'check/check_result.html')





