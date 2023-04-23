from django.forms import ModelForm
from .models import Kaszerowanie

class KaszForm (ModelForm):


    class Meta:
        model = Kaszerowanie
        fields = ("nazwa",
                  "wydruk",
                  "klient",
                  "material",
                  "kasz_zamówienie",
                  "kasz_wykonane",
                  "kasz_gotowe",)
