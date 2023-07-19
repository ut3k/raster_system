
from django.urls import path
from .views import (sztanc_list_all,
                    sztanc_create,
                    sztanc_delete,
                    )


app_name = 'sztancowanie'

urlpatterns = [
    path('', sztanc_list_all, name='sztanc_list_all'),
    path('sztanc_create/',sztanc_create, name='sztanc_create'),
    path('sztanc_delete/<str:pk>',sztanc_delete, name='sztanc_delete'),
    # path('szt/<pk>/', SztancowanieDetailView.as_view(), name='szt_detail'),
    # path('new/', create_view, name='wyk_new'),
    # path('wyk/<id>/update', update_view, name='wyk_update'),
    # path('wyk/<id>/img_update', wyk_img_update, name='wyk_img_update'),
]
