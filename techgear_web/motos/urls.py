from django.urls import path
from . import views

urlpatterns = [
    path('', views.catalogo_motos, name='catalogo'),
    path('login/', views.login_view, name='login'),
    path('registro/', views.registro_view, name='registro'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
]