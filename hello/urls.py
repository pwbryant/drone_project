from django.urls import path
from .views import Hello, Greetings
urlpatterns = [
    path('', Hello.as_view(), name='hello'),
    path('greetings/', Greetings.as_view(), name='greetings'),
]
