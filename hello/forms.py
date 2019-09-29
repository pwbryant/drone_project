from django.forms import ModelForm
from .models import Greeting


class GreetingForm(ModelForm):

    class Meta:
        model = Greeting
        fields = ['greeting']
