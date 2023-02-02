from django import forms
from .models import Kaszerowanie

class KaszForm (forms.ModelForm):


    class Meta:
        model = Kaszerowanie
        fields = ("nazwa",
                  "wydruk",
                  "klient",
                  "material",
                  "kasz_zamówienie",
                  "kasz_wykonane",
                  "kasz_gotowe",)
