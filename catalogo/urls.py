from django.urls import path
from . import views

urlpatterns = [
    path('', views.tienda_inicio, name='index'),
]