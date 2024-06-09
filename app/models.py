from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    is_doctor = models.BooleanField("Is doctor", default=False)
    is_labmember = models.BooleanField("Is doctor", default=False)
    is_patient = models.BooleanField("Is patient", default=False)
    blood_test_doctor = models.CharField(max_length=255, default='')
    x_ray_doctor = models.CharField(max_length=255, default='')


class TestPackage(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

class UserGeneralInfo(models.Model):
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)


class Results(models.Model):
    id=models.PositiveBigIntegerField(auto_created=True,primary_key=True)
    result_id=models.PositiveBigIntegerField()
    value=models.FloatField()

class VisitDetails(models.Model):
    id=models.PositiveBigIntegerField(auto_created=True,primary_key=True)
    details_id=models.PositiveBigIntegerField()
    drugs=models.CharField(max_length=255)
    description=models.CharField(max_length=255)

class HealthPatientHistory(models.Model):
    id=models.PositiveBigIntegerField(auto_created=True,primary_key=True)
    health_id=models.PositiveBigIntegerField()
    date=models.DateField()
    doctor=models.CharField(max_length=255)
    details_id=models.ForeignKey(to=VisitDetails,on_delete=models.CASCADE)

# class PatientResults(models.Model):
#     id=models.PositiveBigIntegerField(auto_created=True,primary_key=True)
#     name=models.ForeignKey(to=Results,on_delete=models.CASCADE)

class Tests(models.Model):
    id=models.PositiveBigIntegerField(auto_created=True,primary_key=True)
    test_id=models.PositiveBigIntegerField()
    name=models.CharField(max_length=255)
    doctor=models.CharField(max_length=255)
    order_date=models.DateField()
    executive_date=models.DateField()
    result_id=models.ForeignKey(to=Results,on_delete=models.CASCADE)
    price=models.FloatField()

class Patients(models.Model):
    id=models.PositiveBigIntegerField(auto_created=True,primary_key=True)
    name=models.CharField(max_length=255)
    surname=models.CharField(max_length=255)  
    age=models.PositiveIntegerField()
    gender=models.CharField(max_length=255)  
    phone=models.CharField(max_length=255)  
    address=models.CharField(max_length=255)  
    health_id=models.ForeignKey(to=HealthPatientHistory,on_delete=models.CASCADE)
    test_id=models.ForeignKey(to=Tests,on_delete=models.CASCADE)

