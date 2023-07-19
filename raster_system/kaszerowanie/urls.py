from django.urls import path
from .views import (KaszerowanieDetailView,
                    kasz_list_todo,
                    kasz_list_done,
                    kasz_list_all,
                    kasz_create,
                    kasz_update,
                    kasz_delete,
                    )


app_name = 'kaszerowanie'

urlpatterns = [
    # path('', KaszerowanieListView.as_view(), name='kasz_list'),
    path('todo', kasz_list_todo , name='kasz_list_todo'),
    path('', kasz_list_all , name='kasz_list_all'),
    path('done', kasz_list_done , name='kasz_list_done'),
    path('kasz/<pk>/', KaszerowanieDetailView.as_view(), name='kasz_detail'),
    path('kasz_create/',kasz_create, name='kasz_create'),
    path('kasz_update/<str:pk>',kasz_update, name='kasz_update'),
    path('kasz_delete/<str:pk>',kasz_delete, name='kasz_delete'),
]
