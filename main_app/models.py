from django.db import models

# Create your models here.
class Enquiry(models.Model):
    name = models.CharField(max_length=20)
    mobile = models.IntegerField()
    email = models.EmailField()
    age = models.IntegerField()
    gender = models.CharField(max_length=10)

class Plans(models.Model):
    plan_name = models.CharField(max_length=30)
    plan_amount = models.IntegerField()
    plan_duration = models.IntegerField()

class Equipments(models.Model):
    equipment_name = models.CharField(max_length=30)
    equipment_price = models.IntegerField()
    unit = models.IntegerField()
    purchased_date = models.DateField()
    description = models.CharField(max_length=255)