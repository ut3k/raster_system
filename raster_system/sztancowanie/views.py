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


def sztanc_delete(request,pk):
    sztanc_item = Sztancowanie.objects.get(id=pk)
    title = str(sztanc_item.pk)
    context = {
            "sztanc":sztanc_item,
            "title":title,
            }
    if request.method=="POST":
        sztanc_item.delete()
        return redirect("sztancowanie:sztanc_list_all")
    return render(request, "sztanc_delete.html", context)


def sztanc_update(request,pk):
    sztanc_item = Sztancowanie.objects.get(id=pk)
    title = "Aktualizacja" + str(sztanc_item.pk)
    context = {
            "sztanc":sztanc_item,
            "title":title
            }
    if request.method == "POST":
        form = SztancForm(request.POST, instance = sztanc_item)
        if form.is_valid():
            form.save()
        return redirect("sztancowanie:sztanc_list_all")
    
    return render(request, "sztanc_update.html", context )

