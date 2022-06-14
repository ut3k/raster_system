from django.urls import path
from .views import (WykrojnikiDetailView,
                    WykrojnikiListView, create_view, update_view,
                    wyk_img_update)

app_name = 'wykrojniki'

urlpatterns = [
    path('', WykrojnikiListView.as_view(), name='wyk_list'),
    path('wyk/<pk>/', WykrojnikiDetailView.as_view(), name='wyk_detail'),
    path('new/', create_view, name='wyk_new'),
    path('wyk/<id>/update', update_view, name='wyk_update'),
    path('wyk/<id>/img_update', wyk_img_update, name='wyk_img_update'),
]
