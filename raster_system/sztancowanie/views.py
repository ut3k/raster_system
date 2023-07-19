from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import HttpResponseRedirect, get_object_or_404, render, redirect
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

# from .forms import WykForm, WykImgUpdateFrom
from .models import Sztancowanie

from .forms import SztancForm

# Create your views here.
# Lista wszystkich zadań sztancowania
def sztanc_list_all(request):
    sztanc_all_set= Sztancowanie.objects.all().order_by("-mod_date")
    sztanc_all_title = "wszystkie zadania"
    sztanc_page_number = request.GET.get('page')
    paginator = Paginator(sztanc_all_set, 8)

    try:
        kasz_all = paginator.page(sztanc_page_number)
    except PageNotAnInteger:
        kasz_all = paginator.page(1)
    except EmptyPage:
        kasz_all = paginator.page(paginator.num_pages)

    context = {
            "kasz_tab_data":kasz_all,
            "title":sztanc_all_title,
            "paginator_data":kasz_all
            }
    return render(request,"sztanc_list_table.html", context)


# sztanc CREATE 
def sztanc_create(request):
    title = "Nowe zadanie"
    form = SztancForm()

    if request.method == 'POST':
        form = SztancForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("sztancowanie:szt_list_all")



    context = {
            "title": title,
            "form":form
            }

    return render(request, "sztanc_create.html", context )
# class SztancowanieListView(ListView):
#     model = Sztancowanie
#     template_name = "sztan_list_view.html"
#     paginate_by = 10

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         return context


# class SztancowanieDetailView(DetailView):
#     model = Sztancowanie
#     template_name = "sztan_detail_view.html"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         return context
