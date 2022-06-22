from django.utils import timezone
from django.db import models

# Create your models here.


class Sztancowanie(models.Model):
    nazwa = models.CharField(max_length=80)
    klient = models.CharField(max_length=80)
    # TODO szt_kod = unikalny klucz
    wykrojnik = models.CharField(max_length=30)
    szt_zamówienie = models.DecimalField(max_digits=10, decimal_places=0)
    szt_wykonane = models.DecimalField(max_digits=10, decimal_places=0)
    szt_gotowe = models.BooleanField(default=False)
    szt_plan_date = models.DateField(default=timezone.now())
    created_date = models.DateTimeField(auto_now_add=True)
    # created_by =
    mod_date = models.DateTimeField(auto_now=True)
    # mod_by =

    def __str__(self):
        return str(self.klient + " - " + self.nazwa)
