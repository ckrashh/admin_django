from django.urls import path
from . import views

urlpatterns = [
    path('', views.AdminView.as_view(), name='admin'),
    path('editar', views.EditarView.as_view(), name='editar'),
    path('agregar', views.AgregarView.as_view(), name='agregar'),
    path('eliminar', views.EliminarView.as_view(), name='eliminar'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]