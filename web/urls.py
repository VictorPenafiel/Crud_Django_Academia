from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('getregion/', views.getregion, name='getregion'),
    path('detalle/', views.detalle, name='detalle'),
]


