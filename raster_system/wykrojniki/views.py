from multiprocessing import context
from django.shortcuts import HttpResponseRedirect, get_object_or_404, render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from .forms import WykForm
from .models import Wykrojniki

# Create your views here.


class WykrojnikiListView(ListView):
    model = Wykrojniki
    template_name = 'wyk_list_view.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class WykrojnikiDetailView(DetailView):
    model = Wykrojniki
    template_name = 'wyk_detail_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


def create_view(request):
    context = {}
    form = WykForm(request.POST or None)
    if form.is_valid():
        form.save()
    context["form"] = form
    return render(request, "wyk_create.html", context)


def update_view(request, id):
    context = {}
    obj = get_object_or_404(Wykrojniki, id=id)
    form = WykForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/wyk/'+id)

    context["form"] = form
    return render(request, "wyk_update.html", context)
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
