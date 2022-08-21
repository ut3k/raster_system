from django.urls import path
from .views import KaszerowanieDetailView, KaszerowanieListView, kasz_list

app_name = 'kaszerowanie'

urlpatterns = [
    # path('', KaszerowanieListView.as_view(), name='kasz_list'),
    path('', kasz_list , name='kasz_list'),
    path('kasz/<pk>/', KaszerowanieDetailView.as_view(), name='kasz_detail'),
]
