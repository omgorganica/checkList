from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class VehicleType(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/', default='None')

    def __str__(self):
        return self.name


class VehicleUnit(models.Model):
    registred_number = models.TextField(max_length=30)
    vehicle_type = models.ForeignKey(VehicleType, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.vehicle_type} № {self.registred_number} '


class Questionnaire(models.Model):
    date = models.DateTimeField(auto_now=True)
    vehicle_type = models.CharField(max_length=50, null=False, blank=False)
    registred_number = models.CharField(max_length=50, null=True, blank=False, default=1)
    user = models.CharField(max_length=50, null=False, blank=False, default=1)
    q1 = models.BooleanField(default=False, blank=True)
    q2 = models.BooleanField(default=False, blank=True)
    q3 = models.BooleanField(default=False, blank=True)
    q4 = models.BooleanField(default=False, blank=True)
    q5 = models.BooleanField(default=False, blank=True)
    q6 = models.BooleanField(default=False, blank=True)
    q7 = models.BooleanField(default=False, blank=True)
    q8 = models.BooleanField(default=False, blank=True)
    q9 = models.BooleanField(default=False, blank=True)
    q10 = models.BooleanField(default=False, blank=True)
    q11 = models.IntegerField(blank=False, validators=[
        MaxValueValidator(100),MinValueValidator(1)
    ])
    q12 = models.CharField(max_length=200, blank=True)
