from django.forms import ModelForm
from .models import Paciente

class PacienteForm(ModelForm):
    class Meta:
        model = Paciente
        fields = [
            'nombre',
            'apellidos',
            'cedula',
            'fecha_nacimiento',
            'sexo',
            'telefono',
            'email',
            'direccion',
            'seguro_medico',
            'grupo_sanguineo',
            'alergias_observaciones',
        ]
