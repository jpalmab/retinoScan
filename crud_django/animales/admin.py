from django.contrib import admin
from .models import Animal
# Register your models here.


#registramos nuestra aplicacion en el panel de admin de django
admin.site.register(Animal)