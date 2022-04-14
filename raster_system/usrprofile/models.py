from django.db import models

# Create your models here.


class usrProfile (modles.Model):
    imię = models.CharField(max_length=30)
    nazwisko = models.CharField(max_lenght=30)
    ksywka = models.CharField(max_length=30)

    del __str__(self):
        return str(self.imię + " " + self.nazwisko)
