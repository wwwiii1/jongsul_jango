from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.
class checkPageView(TemplateView):
    template_name = 'check/check.html'

    def get_context_data(self, **kwargs):
        context = super(checkPageView, self).get_context_data(**kwargs)
        return context
