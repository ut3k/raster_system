from django.forms import ModelForm
from django.utils.functional import classproperty
from .models import Sztancowanie

class SztancForm(ModelForm):


    class Meta:
        model = Sztancowanie
        fields =("nazwa",
                 "klient",
                 "wykrojnik",
                 "szt_zamówienie",
                 "szt_wykonane",
                 "szt_gotowe",
                 "szt_plan_date",
                 )
