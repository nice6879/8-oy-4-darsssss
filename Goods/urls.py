from django.urls import path, include
from Goods import views



urlpatterns = [
    path('', views.main, name='index'),
    path('serializers/', include('Goods.back-office.info.urls')),
    path('authentication/', include('api.urls')),
    path('mycart/', views.mycart_view, name='mycart'),
    path('auth/', include('Goods.authentication.urls')),
    path('user/', include('Goods.user.urls'))

    
]