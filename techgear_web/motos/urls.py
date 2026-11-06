from django.urls import path
from . import views

urlpatterns = [
    path('', views.catalogo_motos, name='catalogo'),
    path('moto/<int:moto_id>/', views.detalle_moto, name='detalle_moto'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('registro/', views.registro_view, name='registro'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
]