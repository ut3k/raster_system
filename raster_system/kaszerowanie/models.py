from django.db import models

# Create your models here.


class Kaszerowanie(models.Model):
    nazwa = models.CharField(max_length=80)
    klient = models.CharField(max_length=80)
    wydruk = models.CharField(max_length=80)
    kasz_zamówienie = models.DecimalField(max_digits=10, decimal_places=0)
    kasz_wykonane = models.DecimalField(max_digits=10, decimal_places=0)
    kasz_gotowe = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    # created_by =
    mod_date = models.DateTimeField(auto_now=True)
    # mod_by =

    def __str__(self):
        return str(self.klient + " - " + self.nazwa)
