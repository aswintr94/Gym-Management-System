from django.db import models

# Create your models here.
class Enquiry(models.Model):
    name = models.CharField(max_length=20)
    mobile = models.IntegerField()
    email = models.EmailField()
    age = models.IntegerField()
    gender = models.CharField(max_length=10)