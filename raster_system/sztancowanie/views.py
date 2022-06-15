from multiprocessing import context
from django.shortcuts import HttpResponseRedirect, get_object_or_404, render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

# from .forms import WykForm, WykImgUpdateFrom
from .models import Sztancowanie

# Create your views here.


class SztancowanieListView(ListView):
    model = Sztancowanie
    template_name = "sztan_list_view.html"
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class SztancowanieDetailView(DetailView):
    model = Sztancowanie
    template_name = "sztan_detail_view.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
