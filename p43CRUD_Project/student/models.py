from django.db import models
CHOICES=[('M','Male'),('F','Female')]

# Create your models here.
class user(models.Model):
    name=models.CharField(max_length=70)
    email=models.EmailField(max_length=100)
    password=models.CharField(max_length=70)
    gender=models.CharField(choices=CHOICES,max_length=2)
    birth_date=models.DateField(blank=True,null=True)