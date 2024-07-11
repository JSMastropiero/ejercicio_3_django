from django.urls import path
from . import views

urlpatterns = [
    path('', views.generar_matriz, name='generar_matriz'),
    path('ver/<int:matriz_id>/', views.ver_matriz, name='ver_matriz'),
    path('ordenar/<int:matriz_id>/', views.ordenar_matriz, name='ordenar_matriz'),
    path('espejar/<int:matriz_id>/', views.espejar_matriz, name='espejar_matriz'),
    path('matrices/', views.listar_matrices, name='listar_matrices'),
]

