from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class Hello(TemplateView):
    template_name = 'hello/base.html'

