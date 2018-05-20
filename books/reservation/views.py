from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.
class reservationPageView(TemplateView):
    template_name = 'reservation/index.html'

    def get_context_data(self, **kwargs):
        context = super(reservationPageView, self).get_context_data(**kwargs)
        return context
