from django.db import models


# Create your models here.
class Feature(models.Model):
    title = models.CharField(max_length=100)
    details = models.TextField()
    image = models.CharField(max_length=100)
