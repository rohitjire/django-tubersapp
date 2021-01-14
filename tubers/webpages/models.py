from django.db import models


# Create your models here.
class Slider(models.model):
    headline = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    buttontext = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='media/slider/%Y/')
    created_date = models.DateTimeField(auto_now_add=True)