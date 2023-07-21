from django import forms
from .models import Kaszerowanie

class KaszForm (forms.ModelForm):


    class Meta:
        model = Kaszerowanie
        fields = ("name",
                  "print",
                  "client",
                  "material",
                  "kasz_ordered",
                  "kasz_done",
                  "kasz_status",
                  )


class KaszFormShort (forms.ModelForm):


    class Meta:
        model = Kaszerowanie
        fields = ( "kasz_done",
                  "kasz_status",
                  )
