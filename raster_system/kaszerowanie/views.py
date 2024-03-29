from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import (
    render,
    HttpResponseRedirect,
    get_object_or_404,
    HttpResponse,
    redirect,
)
from django.views.generic import DetailView, ListView

from .forms import KaszForm, KaszFormShort

# Create your views here.
from .models import Kaszerowanie


# list of todo's for kaszerowanie
def kasz_list_todo(request):
    kasz_todo_set = Kaszerowanie.objects.filter(kasz_gotowe="False")
    kasz_todo_title = "zadania do wykonania"
    kasz_todo_page_number = request.GET.get("page")
    paginator = Paginator(kasz_todo_set, 8)

    try:
        kasz_todo = paginator.page(kasz_todo_page_number)
    except PageNotAnInteger:
        kasz_todo = paginator.page(1)
    except EmptyPage:
        kasz_todo = paginator.page(paginator.num_pages)

    context = {
        "kasz_todo": kasz_todo,
        "title": kasz_todo_title,
        "paginator_data": kasz_todo,
    }

    return render(request, "kasz_list_todo.html", context)


def kasz_list_done(request):
    kasz_done = Kaszerowanie.objects.filter(kasz_status="True").order_by(
        "-created_date"
    )
    kasz_done_title = "zadania wykonane"
    return render(
        request,
        "kasz_list_table.html",
        {"kasz_tab_data": kasz_done, "title": kasz_done_title},
    )


# table view all set
def kasz_list_all(request):
    kasz_all_set = Kaszerowanie.objects.all().order_by("-mod_date")
    kasz_all_title = "wszystkie zadania"
    kasz_page_number = request.GET.get("page")
    paginator = Paginator(kasz_all_set, 8)

    try:
        kasz_all = paginator.page(kasz_page_number)
    except PageNotAnInteger:
        kasz_all = paginator.page(1)
    except EmptyPage:
        kasz_all = paginator.page(paginator.num_pages)

    context = {
        "kasz_tab_data": kasz_all,
        "title": kasz_all_title,
        "paginator_data": kasz_all,
    }
    return render(request, "kasz_list_table.html", context)


class KaszerowanieListView(ListView):
    model = Kaszerowanie
    template_name = "kasz_list_view.html"
    # paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class KaszerowanieDetailView(DetailView):
    model = Kaszerowanie
    template_name = "kasz_detail_view.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


# kasz create
def kasz_create(request):
    title = "Nowe zadanie"
    form = KaszForm()

    if request.method == "POST":
        form = KaszForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("kaszerowanie:kasz_list_all")

    context = {"title": title, "form": form}

    return render(request, "kasz_create.html", context)


# kasz UPDATE
def kasz_update(request, pk):
    title = "Aktualizacja"
    kasz_item = Kaszerowanie.objects.get(id=pk)
    form = KaszForm(instance=kasz_item)

    if request.method == "POST":
        form = KaszForm(request.POST, instance=kasz_item)
        if form.is_valid():
            form.save()
            return redirect("kaszerowanie:kasz_list_all")

    context = {"title": title, "form": form, "kasz": kasz_item}
    return render(request, "kasz_update.html", context)


# Kasz DELETE
def kasz_delete(request, pk):
    kasz_item = Kaszerowanie.objects.get(id=pk)
    context = {
        "kasz": kasz_item,
    }
    if request.method == "POST":
        kasz_item.delete()
        return redirect("kaszerowanie:kasz_list_all")
    return render(request, "kasz_delete.html", context)


# Quick status
def kasz_status_done(request, pk):
    kasz_item = Kaszerowanie.objects.get(id=pk)
    form = KaszFormShort(instance=kasz_item)
    title = "zadanie wykonane?"
    context = {
        "title": title,
        "kasz": kasz_item,
        "form": form,
    }
    if request.method == "POST":
        form = KaszFormShort(request.POST, instance=kasz_item)
        if form.is_valid():
            form.save()
            return redirect("kaszerowanie:kasz_list_all")

    return render(request, "kasz_status_done.html", context)
