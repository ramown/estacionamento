# urls.py
from django.urls import path, re_path
from core import views


urlpatterns = [
    path('', views.index, name='home'),
    path('monitor/', views.monitor_page, name='monitor'),
    path('estacionamento/<int:id>/', views.index_estacionamento, name='index_estacionamento'),
    path('estacionamento/new/', views.new_estacionamento, name='new_estacionamento'),
    path('liberar/vaga/<int:id_vaga>/', views.liberar_vaga, name='liberar_vaga'),
    path('selecionar/veiculo/<int:id_veiculo>/', views.selecionar_veiculo, name='selecionar_veiculo'),
    path('ocupar/vaga/<int:id_vaga>/veiculo/<int:id_veiculo>/', views.ocupar_vaga, name='ocupar_vaga'),
    ]

