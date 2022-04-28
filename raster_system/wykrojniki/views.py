from multiprocessing import context
from django.shortcuts import render
from .models import Wykrojniki
from django.views.generic.list import ListView

# Create your views here.


class WykrojinikiListView(ListView):
    model = Wykrojniki
    template_name = 'test.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


# def home_view(request, **kwargs):
# def home_view(request):
#     model = Wykrojniki

#     context = {
#         "tresc": "tresc 1",
#         "liczba1": 12,
#         "napis": "treść napisu"
#     }
#     # pk = kwargs.get("pk")
#     # wyk = Wykrojniki.objects.get(pk=pk)

#     # return render(request, 'detail.html', {"wykrojnik": wyk})
#     return render(request, 'test.html', context)
