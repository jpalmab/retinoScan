from django.db import models

# Create your models here.
#orm / object relational mapping
class Animal(models.Model):
    name = models.CharField(max_length=100, blank = False, null = False)
    especie = models.CharField(max_length=100, blank = False, null = False)

    def __str__(self):
        return self.name
    
class Usuario(models.Model):
    nombre = models.CharField(max_length=250, null=True, blank=True)
    celular = models.CharField(max_length=13, null=True, blank=True)
    username = models.CharField(max_length=100, unique = True)
    password = models.CharField(max_length=255)
    email = models.CharField(max_length=100, null=True, blank=True)
    activo = models.BooleanField(default=True)
    last_login = models.DateTimeField(null=True, blank=True)


    class Meta:
        db_table = 'usuarios' #tabla de mysql
        managed = False

        
    def __str__(self):
        return self.username
    
    #Django necesita estas propiedades para el sistema de autenticación
    @property
    def is_authenticated(self):
        return True
    @property
    def is_anonymous(self):
        return False #nunca es anónimo si pasó el login
    @property
    def is_active(self):
        return self.activo #usa tu campo "activo" de la base de datos para determinar si el usuario está activo o no


class Paciente(models.Model):
    SEXO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Femenino'),
    ]
    GRUPO_CHOICES = [
        ('A+', 'A+'), ('A-', 'A-'),
        ('B+', 'B+'), ('B-', 'B-'),
        ('AB+', 'AB+'), ('AB-', 'AB-'),
        ('O+', 'O+'), ('O-', 'O-'), 
    ]
    
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    cedula = models.CharField(max_length=20, unique=True)
    fecha_nacimiento = models.DateField()
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)
    telefono = models.CharField(max_length=13, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    direccion = models.TextField(blank=True, null=True)
    seguro_medico = models.CharField(max_length=150, blank=True, null=True)
    grupo_sanguineo = models.CharField(max_length=3, choices=GRUPO_CHOICES, blank=True, null=True)
    alergias_observaciones = models.TextField(blank=True, null=True)
    
    class Meta:
        db_table = 'paciente' #nombre de la tabla en mysql
        managed = False #Django gestionará esta tabla, pero no intentará crearla ni modificarla automáticamente
    
    def __str__(self):
        return f"{self.nombre} {self.apellidos}"