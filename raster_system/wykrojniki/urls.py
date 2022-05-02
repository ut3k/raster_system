from django.urls import path
from .views import WykrojnikiDetailView, WykrojnikiListView, create_view

app_name = 'wykrojniki'

urlpatterns = [
    path('', WykrojnikiListView.as_view(), name='wyk_list'),
    path('wyk/<pk>/', WykrojnikiDetailView.as_view(), name='wyk_detail'),
    path('new/', create_view, name='wyk_new')

]
