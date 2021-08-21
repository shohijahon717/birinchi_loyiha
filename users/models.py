from django.db import models
from django.contrib.auth.models import AbstractUser  #auth bilan ishlash uchun
# Create your models here.
class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)
    address = models.CharField(max_length=300)
    job = models.CharField(max_length=100)
