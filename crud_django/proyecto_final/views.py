from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Paciente
from .forms import PacienteForm


# -- AUTENTICACIÓN --

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        usuario = authenticate(request, username=username, password=password)
        if usuario:
            login(request, usuario)
            return redirect('aplication:lista_pacientes')
        else:
            return render(request, 'retinoscan/login.html', {'error': 'Credenciales inválidas'})
    return render(request, 'retinoscan/login.html')

def logout_view(request):
    if request.method == 'POST':
        logout(request)
    return redirect('aplication:login')


# -- CRUD PACIENTES --

@login_required
def lista_pacientes(request):
    pacientes = Paciente.objects.all()
    return render(request, 'retinoscan/lista_pacientes.html', {'pacientes': pacientes})

@login_required
def crear_paciente(request):
    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('aplication:lista_pacientes')
    else:
        form = PacienteForm()
    return render(request, 'retinoscan/crear_paciente.html', {'form': form})

@login_required
def editar_paciente(request, id):
    paciente = get_object_or_404(Paciente, id=id)
    if request.method == 'POST':
        form = PacienteForm(request.POST, instance=paciente)
        if form.is_valid():
            form.save()
            return redirect('aplication:lista_pacientes')
    else:
        form = PacienteForm(instance=paciente)
    return render(request, 'retinoscan/editar_paciente.html', {'form': form})

@login_required
def eliminar_paciente(request, id):
    paciente = get_object_or_404(Paciente, id=id)
    if request.method == 'POST':
        paciente.delete()
        return redirect('aplication:lista_pacientes')
    return render(request, 'retinoscan/confirmar_eliminar_paciente.html', {'paciente': paciente})


#CRUD EXAMENES (PENDIENTE)
@login_required
def crear_examen(request, id):
    return render(request, 'retinoscan/crear_examen.html')

@login_required
def lista_examen(request):
    return render(request, 'retinoscan/lista_examen.html')
