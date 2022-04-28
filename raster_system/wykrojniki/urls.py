from django.urls import path
from .views import WykrojinikiListView

app_name = 'wykrojniki'

urlpatterns = [
    path('', WykrojinikiListView.as_view(), name='wyk_list'),
]
