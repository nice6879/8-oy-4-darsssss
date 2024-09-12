from django.urls import path
from .views import info_list, info_create, info_delete, info_update, info_detail

urlpatterns = [
    path('info_list', info_list, name='info_list'),
    path('info_create', info_create, name='info_create'),
    path('info_delete/<int:pk>', info_delete, name='info_delete'),
    path('info_update/<int:pk>', info_update, name='info_update'),
    path('info_detail/<int:pk>', info_detail, name='info_detail'),

]