from django.urls import path
from animales import views as v


app_name = 'aplication'
urlpatterns = [
    path('', v.lista_pacientes , name='inicio'),
    path('detail_<int:id>/',v.detail, name='detail'),
    path('create/', v.create_animal, name='create'),
    path('update_<int:id>/', v.update_animal, name='update'),
    path('delete_<int:id>/', v.delete_animal, name='delete'),
    #Rutas de autenticación
    path('login/', v.login_view, name='login'),
    path('logout/', v.logout_view, name='logout'),
    
  # Rutas de Paciente
    path('pacientes/', v.lista_pacientes, name='lista_pacientes'),
    path('pacientes/crear/', v.crear_paciente, name='crear_paciente'),
    path('pacientes/editar/<int:id>/', v.editar_paciente, name='editar_paciente'),
    path('pacientes/eliminar/<int:id>/', v.eliminar_paciente, name='eliminar_paciente'),
]
