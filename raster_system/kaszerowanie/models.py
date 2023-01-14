from django.utils import timezone
from django.db import models

# Create your models here.


class Kaszerowanie(models.Model):
    nazwa = models.CharField(max_length=80)
    wydruk = models.CharField(max_length=80)
    klient = models.CharField(max_length=80)
    material = models.CharField(max_length=80, default="mikrofala")
    kasz_zamówienie = models.IntegerField(default=0)
    kasz_wykonane = models.IntegerField(default=0)
    kasz_gotowe = models.BooleanField(default=False)
    # kasz_plan_date = models.DateField(default=timezone.now())
    created_date = models.DateTimeField(auto_now_add=True)
    # created_by =
    mod_date = models.DateTimeField(auto_now=True)
    # mod_by =

    def __str__(self):
        return str(self.klient + " - " + self.nazwa)
