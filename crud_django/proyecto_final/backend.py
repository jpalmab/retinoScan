from django.contrib.auth.hashers import check_password
from .models import Usuario

class UsuarioBackend:
    #Django llama este método cuando se usa authenticate() para autenticar a un usuario
    def authenticate(self, request, username=None, password=None):
        try:
            #Busca en la tabla "usuarios" por username y que esté activo
            usuario = Usuario.objects.get(username=username, activo=True)

            #check_password compara la contraseña escrita con el hash guardado en la B.D
            if check_password(password, usuario.password):
                return usuario #login exitoso, devuelve el usuario
            return None #contraseña incorrecta
        except Usuario.DoesNotExist:
            return None #Usuario no existe en la base de datos
        
    #Django llama este método para recuperar el usuario de la sesión activa
    def get_user(self, user_id):
        try:
            return Usuario.objects.get(pk=user_id) #Busca el usuario por su ID
        except Usuario.DoesNotExist:
            return None #la sesión expiró o el usuario fue eliminado

