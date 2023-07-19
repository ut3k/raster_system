from django import forms
from .models import Wykrojniki


class WykForm(forms.ModelForm):
    class Meta:
        model = Wykrojniki
        fields = [
            "name",
            "wyk_size",
            "wyk_kod",
            "wyk_image",
            "wyk_pdf",
            "wyk_cdr",
        ]


class WykImgUpdateFrom(forms.ModelForm):
    class Meta:
        model = Wykrojniki
        fields = ["wyk_image"]


# class WykPdfUpdateFrom(forms.ModelForm):
#     class Meta:
#         model = Wykrojniki
#         fields = ["wyk_pdf"]


# class WykCdrUpdateFrom(forms.ModelForm):
#     class Meta:
#         model = Wykrojniki
#         fields = ["wyk_cdr"]
