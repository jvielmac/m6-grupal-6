from django.shortcuts import render, redirect
from .forms import RegistroUsuarioForm
from django.contrib import messages
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required


def registro(request):
    if request.method == "POST":
        formulario_p = RegistroUsuarioForm(request.POST)
        if formulario_p.is_valid():
            usuario = formulario_p.save(commit=False)
            grupo_seleccionado = formulario_p.cleaned_data["grupo"]
            if grupo_seleccionado == 'admin':
                grupo = Group.objects.get(name='admin')
            elif grupo_seleccionado == 'compras':
                grupo = Group.objects.get(name='compras')
            elif grupo_seleccionado == 'moderador':
                grupo = Group.objects.get(name='moderador')
            usuario.save()
            usuario.groups.add(grupo)

            username = formulario_p.cleaned_data["username"]
            messages.success(request, f'Cuenta creada de forma exitosa para usuario {username}')
            return redirect('crear-cliente')
        else:
            messages.error(request, f'Error al registrarse')
    formulario = RegistroUsuarioForm()

    return render(request, "usuarios/registro.html", {'formulario': formulario})


@login_required
def perfil(request):
    return render(request, 'usuarios/perfil.html', {'user': request.user})