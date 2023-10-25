from django.utils import timezone
from django.db import models

# Create your models here.


class Kaszerowanie(models.Model):
    name = models.CharField(max_length=80)
    print = models.CharField(max_length=80)
    client = models.CharField(max_length=80)
    material = models.CharField(max_length=80, default="mikrofala")
    kasz_ordered = models.IntegerField(default=0)
    kasz_done = models.IntegerField(default=0)
    kasz_status = models.BooleanField(default=False)
    kasz_plan_date = models.DateField(default=timezone.now)
    created_date = models.DateTimeField(auto_now_add=True)
    # created_by =
    mod_date = models.DateTimeField(auto_now=True)
    # mod_by =
    # def save(self, modified_fields):
    #     super().save(Kaszerowanie)
    #     KaszerowanieLog.create(modified_fields=)


    # def __str__(self):
    #     return str(self.klient + " - " + self.nazwa)
