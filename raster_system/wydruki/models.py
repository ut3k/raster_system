from django.utils import timezone
from django.db import models

# Create your models here.


class Wydruki(models.Model):
    nazwa = models.CharField(max_length=80)
    klient = models.CharField(max_length=80)
    # TODO: kody QR dla wydruków
    # wyd_kod = models.CharField(max_length=16, unique=True)
    wyd_roz_sze = models.DecimalField(
        max_digits=10, decimal_places=2, help_text="szerokość w mm")
    wyd_roz_wys = models.DecimalField(
        max_digits=10, decimal_places=2, help_text="wysokość w mm")
    wyd_zamówienie = models.IntegerField(default=0)
    wyd_wykonane = models.IntegerField(default=0)
    wyd_gotowe = models.BooleanField(default=False)
    wyd_plan_date = models.DateField(default=timezone.now())
    created_date = models.DateTimeField(auto_now_add=True)
    # created_by =
    mod_date = models.DateTimeField(auto_now=True)
    # mod_by =

    def __str__(self):
        return str(self.klient + " - " + self.nazwa)
