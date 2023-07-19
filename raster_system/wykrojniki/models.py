from django.db import models

# Create your models here.


class Wykrojniki(models.Model):
    name = models.CharField(max_length=120)
    # group = models.ForeignKey(wyk_group)
    wyk_kod = models.CharField(max_length=16)
    wyk_size = models.CharField(
        max_length=12, help_text="wymiary w milimetrach")
    # TODO - przygotuj skaner QR
    # wyk_qr = models.ImageField(upload_to="wykrojniki_qr", blank=True)
    wyk_image = models.ImageField(upload_to="wykrojniki_img/", blank=True)
    wyk_pdf = models.FileField(upload_to="wykrojniki_pdf/", blank=True)
    wyk_cdr = models.FileField(upload_to="wykrojniki_cdr/", blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    # created_by =
    mod_date = models.DateTimeField(auto_now=True)
    # mod_by =

    def __str__(self):
        return str(self.nazwa)


class wyk_group(models.Model):
    nazwa = models.CharField(max_length=120)
