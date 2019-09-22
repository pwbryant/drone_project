from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Greeting

# Create your views here.
class Hello(TemplateView):
    template_name = 'hello/base.html'

class Greetings(ListView):
    model = Greeting
    template_name = 'hello/greetings.html'

