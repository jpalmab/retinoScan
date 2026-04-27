from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Animal, Paciente
from .forms import AnimalForm, PacienteForm


# Create your views here.
#vistas usadas en funciones no en clases
# --------------------
# -- CRUD ANIMALES --
# --------------------

@login_required #LOGIN REQUERIDO PARA VER LA PAGINA DE INICIO
def inicio(request):
    animales = Animal.objects.all()
    context = {
        'animales': animales
    }
    return render(request, 'animales/inicio.html', context)

@login_required #LOGIN REQUERIDO PARA VER EL DETALLE DE UN ANIMAL
def detail(request, id):
    detail_animal = get_object_or_404(Animal, pk=id)
    context = {
        'detail_animal':detail_animal
    }
    return render(request, 'animales/detail.html', context)

@login_required #LOGIN REQUERIDO PARA CREAR UN ANIMAL
def create_animal(request):
    if request.method == 'POST':
        animal_form = AnimalForm(request.POST)
        if animal_form.is_valid():
            animal_form.save()
            return redirect('aplication:inicio')
    else:
        animal_form = AnimalForm()

    return render(request, 'animales/create.html',{'animal_form':animal_form})    

@login_required #LOGIN REQUERIDO PARA EDITAR UN ANIMAL
def update_animal(request, id):
    animal = get_object_or_404(Animal, id=id)
    if request.method == 'POST':
        animal_form = AnimalForm(request.POST, instance=animal)
        if animal_form.is_valid():
            animal_form.save()
            return redirect('aplication:inicio')
    else:
         animal_form = AnimalForm(instance=animal)
         return render(request, 'animales/editar.html',{'animal_form':animal_form}) 

@login_required #LOGIN REQUERIDO PARA ELIMINAR UN ANIMAL
def delete_animal(request, id):
    animal = get_object_or_404(Animal, id=id)
    if animal: #si el animal existe
        animal.delete() #elimina el animal
        return redirect('aplication:inicio') #redirecciona a la pagina de inicio
    


#-- LOGIN - -
def login_view(request):
    if request.method == 'POST':
        #Captura lo que el usuario escribió en el formulario de login|
        username = request.POST['username']
        password = request.POST['password']

        #authenticate() llama a UsuarioBackend y verifica las credenciales
        usuario = authenticate(request, username=username, password=password)

        if usuario:
            #login() crea la sesión del usuario en el navegador
            login(request, usuario)
            return redirect('aplication:inicio')
        else:
            #Si las credenciales son incorrectas, muestra un mensaje de error 
            #en el template de login
            return render(request, 'animales/login.html', {'error': 'Credenciales inválidas'})
    #Si es GET simplemente muestra el formulario vacío
    return render(request, 'animales/login.html')

def logout_view(request):
    #Destruye la sesión activa del usuario
    if request.method == 'POST':
        logout(request)
    return redirect('aplication:login')


# --------------------
# -- CRUD PACIENTES --
# --------------------

#listar los pacientes
@login_required
def lista_pacientes(request):
    pacientes = Paciente.objects.all()
    return render (request, 'animales/lista_pacientes.html', {'pacientes': pacientes })


#crear un paciente
@login_required
def crear_paciente(request):
    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('aplication:lista_pacientes')
    else:
        form = PacienteForm()
            
    return render (request, 'animales/crear_paciente.html', {'form':form})

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
    return render (request, 'animales/editar_paciente.html', {'form':form})

@login_required
def eliminar_paciente(request, id):
    paciente = get_object_or_404(Paciente, id=id)
    if request.method == 'POST':
        paciente.delete()
        return redirect('aplication:lista_pacientes')
    return render (request, 'animales/confirmar_eliminar_paciente.html', {'paciente':paciente})

        
    

