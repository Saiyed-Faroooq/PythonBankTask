from django.db import models

# Create your models here.


class District(models.Model):
    name = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return self.name


class Branch(models.Model):
    district = models.ForeignKey(District, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return self.name

