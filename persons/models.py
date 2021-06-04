from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

class Characters(models.Model):
    character_name = models.CharField(max_length=50)
    real_name = models.CharField(max_length=50)
    image = models.CharField(max_length=2000, default=0)
    dob = models.CharField(max_length=30)
    age = models.IntegerField(default=0)
    movies = models.CharField(max_length=5000)
    awards = models.CharField(max_length=500)
    external_links = models.CharField(max_length=1000)

    def get_absolute_url(self):
        return reverse('persons:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.character_name

class TestForm(models.Model):
    name = models.CharField(max_length=50)
    Test_Img = models.ImageField(upload_to='images/')

