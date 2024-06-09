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


# class Results(models.Model):
#     id=models.AutoField(primary_key=True, null=False)
#     value=models.FloatField(default=1.0)
#     value1=models.FloatField(default=1.0)
#     result_id = models.PositiveBigIntegerField(blank=True,null=True)

# class VisitDetails(models.Model):
#     id=models.AutoField(primary_key=True, null=False)
#     details_id=models.PositiveBigIntegerField(blank=True,null=True)
#     drugs=models.CharField(max_length=255)
#     description=models.CharField(max_length=255)

class HealthPatientHistory(models.Model):
    id=models.AutoField(primary_key=True, null=False)
    health_id=models.PositiveBigIntegerField(blank=True,null=True)
    date=models.DateField()
    doctor=models.CharField(max_length=255)
    # details_id=models.ForeignKey(blank=True,null=True,to=VisitDetails,on_delete=models.CASCADE)

# class PatientResults(models.Model):
#     id=models.AutoField(primary_key=True, null=False)
#     name=models.ForeignKey(blank=True,null=True,to=Results,on_delete=models.CASCADE)

# class Tests(models.Model):
#     id=models.AutoField(primary_key=True, null=False)
#     test_id=models.PositiveBigIntegerField(blank=True,null=True)
#     name=models.CharField(max_length=255)
#     doctor=models.CharField(max_length=255)
#     order_date=models.DateField()
#     executive_date=models.DateField()
#     # result_id=models.ForeignKey(blank=True,null=True,to=Results,on_delete=models.CASCADE)
#     price=models.FloatField()

class Patients(models.Model):
    id=models.AutoField(primary_key=True, null=False)
    name=models.CharField(max_length=255)
    surname=models.CharField(max_length=255)
    age=models.PositiveIntegerField(blank=True,null=True)
    gender=models.CharField(max_length=255)
    phone=models.CharField(max_length=255)
    address=models.CharField(max_length=255)
    health_id=models.ForeignKey(blank=True,null=True,to=HealthPatientHistory,on_delete=models.CASCADE)
    # test_id=models.ForeignKey(blank=True,null=True,to=Tests,on_delete=models.CASCADE)

