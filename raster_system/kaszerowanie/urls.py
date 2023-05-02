from django.urls import path
from .views import (KaszerowanieDetailView,
                    KaszerowanieListView,
                    kasz_list_todo,
                    kasz_list_done,
                    kasz_list_all,
                    kasz_create,
                    )


app_name = 'kaszerowanie'

urlpatterns = [
    # path('', KaszerowanieListView.as_view(), name='kasz_list'),
    path('todo', kasz_list_todo , name='kasz_list_todo'),
    path('all', kasz_list_all , name='kasz_all_table'),
    path('done', kasz_list_done , name='kasz_list_done'),
    path('kasz/<pk>/', KaszerowanieDetailView.as_view(), name='kasz_detail'),
    path('kasz_create/',kasz_create, name='kasz_create'),
]
