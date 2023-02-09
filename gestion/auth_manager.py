from django.contrib.auth.models import BaseUserManager
#BaseUserManager> sirve para modificar la creacion y administarcion de los auth_user

class UsuarioManager(BaseUserManager):
    #esta clase me permitira modificar la admisnitarcion del ususario mediante el comando createsuperuser
    def create_superuser(self, correo, nombre, apellido, tipoUsuario, password):
        #valido si es que no hay correo
        if not correo:
            raise ValueError('EL usuario no porporciono correo')
        #valido que ele correo cumpla con el formato correcto
        #removera los espcaios al inicio y al final y validara que no se utilice caracateres  incorrectos
        correo_normalizado=self.normalize_email(correo)

        #llamamos al modelo que esatmos utilizando e inicialmente el nuevo ususario
        nuevo_usuario=self.model(correo=correo_normalizado, nombre=apellido, tipoUsuario=tipoUsuario)

        #generamos el hash de la contraseña
        #generar el hash de la contraseña utilizando algoritmos de hash SHA512
        #https://docs.djangoproject.com/en/4.1/ref/contrib/auth/#django.contrib.auth.models.User.set_passw
        
        
        nuevo_usuario.set_password(password)

        nuevo_usuario.is_superuser=True
        nuevo_usuario.is_staff=True

        nuevo_usuario.save()
