from django.forms import ModelForm
from django.utils.functional import classproperty
from .models import Sztancowanie

class SztancForm(ModelForm):


    class Meta:
        model = Sztancowanie
        fields =("name",
                 "client",
                 "wykrojnik",
                 "szt_ordered",
                 "szt_done",
                 "szt_status",
                 "szt_plan_date",
                 )
