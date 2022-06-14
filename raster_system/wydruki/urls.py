from django.urls import path
from .views import (WydrukiDetailView, WydrukiListView)

app_name = 'wydruki'

urlpatterns = [
    path('', WydrukiListView.as_view(), name='wyk_list'),
    path('wyd/<pk>/', WydrukiDetailView.as_view(), name='wyk_detail'),
    # path('new/', create_view, name='wyk_new'),
    # path('wyk/<id>/update', update_view, name='wyk_update'),
    # path('wyk/<id>/img_update', wyk_img_update, name='wyk_img_update'),
]
