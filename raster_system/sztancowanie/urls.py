
from django.urls import path
from .views import SztancowanieDetailView, SztancowanieListView

app_name = 'sztancowanie'

urlpatterns = [
    path('', SztancowanieListView.as_view(), name='szt_list'),
    path('szt/<pk>/', SztancowanieDetailView.as_view(), name='szt_detail'),
    # path('new/', create_view, name='wyk_new'),
    # path('wyk/<id>/update', update_view, name='wyk_update'),
    # path('wyk/<id>/img_update', wyk_img_update, name='wyk_img_update'),
]
