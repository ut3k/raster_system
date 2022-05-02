from django import forms
from .models import Wykrojniki


class WykForm(forms.ModelForm):
    class Meta:
        model = Wykrojniki
        fields = [
            "nazwa",
            "wyk_kod",
            "wyk_image",
            "wyk_pdf",
            "wyk_cdr",
        ]
