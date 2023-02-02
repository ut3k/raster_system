from django.shortcuts import render, HttpResponseRedirect, get_object_or_404, HttpResponse
from django.views.generic import DetailView, ListView
from .forms import KaszForm

# Create your views here.
from .models import Kaszerowanie

def kasz_list(request):
    kasz_zrobic = Kaszerowanie.objects.filter(kasz_gotowe="False")
    kasz_zrobione = Kaszerowanie.objects.filter(kasz_gotowe="True")
    return render(request,"kasz_list_view.html", {"kasz_zrobic":kasz_zrobic, "kasz_zrobione":kasz_zrobione} )

def kasz_list_done(request):
    kasz_done= Kaszerowanie.objects.filter(kasz_gotowe="True").order_by("-created_date")
    kasz_done_title = "Zadania wykonane"
    return render(request,"kasz_list_table.html", {"kasz_tab_data":kasz_done, "kasz_title":kasz_done_title})

def kasz_list_all(request):
    kasz_done= Kaszerowanie.objects.order_by("-created_date")
    kasz_done_title = "Zadania wykonane"
    return render(request,"kasz_list_table.html", {"kasz_tab_data":kasz_done, "kasz_title":kasz_done_title})

class KaszerowanieListView(ListView):
    model = Kaszerowanie
    template_name = "kasz_list_view.html"
    # paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class KaszerowanieDetailView (DetailView):
    model = Kaszerowanie
    template_name = "kasz_detail_view.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

def kasz_new(request):
    form = KaszForm
    return render(request, 'kasz_new.html', {'form':form})
