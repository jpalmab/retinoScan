from django.forms import ModelForm
from .models import Animal, Paciente

class AnimalForm(ModelForm):
    class Meta:
        model = Animal
        fields = '__all__' #['name', 'especie'] son los campos que queremos mostrar en el formulario, si queremos mostrar todos los campos usamos fields = '__all__'


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