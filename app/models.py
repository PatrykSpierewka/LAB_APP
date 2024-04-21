from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    is_doctor = models.BooleanField("Is doctor", default=False)
    is_labmember = models.BooleanField("Is doctor", default=False)
    is_patient = models.BooleanField("Is patient", default=False)


class TestPackage(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()