from django.urls import path
from proyecto_final import views as v

app_name = 'aplication'

urlpatterns = [
    path('login/', v.login_view, name='login'),
    path('logout/', v.logout_view, name='logout'),

    path('', v.lista_pacientes, name='lista_pacientes'),
    path('pacientes/crear/', v.crear_paciente, name='crear_paciente'),
    path('pacientes/editar/<int:id>/', v.editar_paciente, name='editar_paciente'),
    path('pacientes/eliminar/<int:id>/', v.eliminar_paciente, name='eliminar_paciente'),
    path('pacientes/crear_examen/<int:id>/', v.crear_examen, name='crear_examen'),
    path('pacientes/lista_examen/', v.lista_examen, name='lista_examen'),
]
