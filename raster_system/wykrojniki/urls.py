from django.urls import path

app_name = 'wykrojniki'

urlpatterns = [
    path('', list_view, name='wyk_list'),
]
