from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView
from django.views.generic.list import MultipleObjectMixin
from .forms import GreetingForm
from .models import Greeting

# Create your views here.
class Hello(TemplateView):
    template_name = 'hello/base.html'


class Greetings(MultipleObjectMixin, FormView):
    form_class = GreetingForm
    model = Greeting
    success_url = reverse_lazy('greetings')
    template_name = 'hello/greetings.html'

    def get(self, request):
        return super().get(request)

    def get_context_data(self):
        object_list = self.get_queryset()
        context = super().get_context_data(
            object_list=object_list
        )
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset

    def form_valid(self, form):
        form.instance.save()
        return super().form_valid(form)
