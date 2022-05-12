from django.db import models


# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    description = models.TextField()
    date_enrolled = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
