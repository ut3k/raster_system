from multiprocessing import context
from django.shortcuts import render
from .models import Wykrojniki

# Create your views here.


def home_view(request):
    context = {
        "tresc": "tresc 1",
        "liczba1": 12,
        "napis": "treść napisu"
    }
    return render(request, 'test.html', context)
