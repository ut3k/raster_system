
from django.urls import path
from .views import (SztancowanieDetailView, 
                    SztancowanieListView,
                    sztanc_list_all,
                    )


app_name = 'sztancowanie'

urlpatterns = [
    path('', sztanc_list_all, name='szt_list_all'),
    path('szt/<pk>/', SztancowanieDetailView.as_view(), name='szt_detail'),
    # path('new/', create_view, name='wyk_new'),
    # path('wyk/<id>/update', update_view, name='wyk_update'),
    # path('wyk/<id>/img_update', wyk_img_update, name='wyk_img_update'),
]
