from django.db import models

# Create your models here.

class Greeting(models.Model):

    greeting = models.CharField(max_length=10)

    def __str__(self):
        return self.greeting
