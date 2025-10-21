from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import permission_required
from .mixins import  PermissionProtectedTemplateView , CustomLoginRequiredMixin
from django.contrib import messages

class AdminView(PermissionProtectedTemplateView, CustomLoginRequiredMixin):
    template_name = 'admin.html'
    permission_required = 'productos.view_producto'
class AgregarView(PermissionProtectedTemplateView):
    template_name = 'agregar_producto.html'
    group_required = 'Administradores'
    permission_required = 'productos.add_producto'

class EliminarView(PermissionProtectedTemplateView):
    template_name = 'elimar_producto.html'
    group_required = 'Administradores'
    permission_required = 'productos.delete_producto'

class EditarView(PermissionProtectedTemplateView):
    template_name = 'editar_producto.html'
    group_required = 'Administradores'
    permission_required = 'productos.change_producto'

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('admin')
        else:
            messages.error(request, "Usuario o contraseña incorrecta")
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return render(request,'logout.html')
def handler403(request, exception=None):
    """Manejador personalizado para errores 403 (Permiso denegado)"""
    return render(request, '403.html', status=403)


def handler404(request, exception=None):
    """Manejador personalizado para errores 404 (Página no encontrada)"""
    return render(request, '404.html', status=404)