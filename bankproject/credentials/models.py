from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.


class District(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Branch(models.Model):
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    name = models.CharField(max_length=50)
    dob = models.DateField()
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    phone = PhoneNumberField(blank=True)
    address = models.CharField(max_length=250)
    district = models.ForeignKey(District, blank=True, on_delete=models.CASCADE, null=True)
    branch = models.ForeignKey(Branch, blank=True, on_delete=models.CASCADE, null=True)
    account_type = models.CharField(max_length=10)
    materials = models.CharField(max_length=10)

    def __str__(self):
        return self.name

