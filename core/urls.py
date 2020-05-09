# urls.py
from django.urls import path, re_path
from core import views


urlpatterns = [
    path('', views.index, name='home'),
    path('monitor/', views.monitor_page, name='monitor'),
    path('estacionamento/<int:id>/', views.index_estacionamento, name='index_estacionamento'),
    path('estacionamento/new/', views.new_estacionamento, name='new_estacionamento'),
    ]
