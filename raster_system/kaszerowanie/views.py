from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.views.generic import DetailView, ListView

# Create your views here.
from .models import Kaszerowanie


class KaszerowanieListView(ListView):
    model = Kaszerowanie
    template_name = "kasz_list_view.html"
    # paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class KaszerowanieDetailView (DetailView):
    model = Kaszerowanie
    template_name = "kasz_list_view.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
