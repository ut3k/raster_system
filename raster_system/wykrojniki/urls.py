from django.urls import path
from .views import WykrojnikiDetailView, WykrojnikiListView

app_name = 'wykrojniki'

urlpatterns = [
    path('', WykrojnikiListView.as_view(), name='wyk_list'),
    path('<pk>/', WykrojnikiDetailView.as_view(), name='wyk_detail')
]
