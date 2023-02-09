from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .auth_manager import UsuarioManager

class CategoriaModel(models.Model):
    # Si no especificamos la columna ID django lo hara de manera predeterminada con el tipo de dato AutoField y tbn lo colocara como llave primaria
    # https://docs.djangoproject.com/en/4.1/ref/models/fields/#field-types
    id = models.AutoField(primary_key=True, null=False)
    nombre = models.CharField(max_length=50, unique=True) # en la bd creara un varchar con 50 caracteres de longitud maxima
    
    class Meta: 
        # sirve para definir los atributos de la clase que estamos heredando directamente para pasarle la metadata sin utilizar el metodo super
        # sirve para modificar la configuracion y comportamiento de esta tabla en la base de datos
        # https://docs.djangoproject.com/en/4.1/ref/models/options/
        db_table = 'categorias'
        # modificamos el ordenamiento al momento de devolver los registros
        # nombre ascendente (A-Z)
        # nombre descendente (Z-A)
        # como ya sabemos que el nombre jamas se repetira la segunda clausula de ordenamiento esta de mas porque nunca se va a dar
        ordering = ['nombre', 'id']


class PlatoModel(models.Model):
    # id = models.AutoField(primary_key= True, null=False)
    nombre = models.CharField(max_length=50, unique=True, null=False)
    precio = models.FloatField()
    disponibilidad = models.BooleanField(default=True)
    # auto_now_add > cada vez que cree un nuevo registro su valor sera la hora y fecha actual del servidor de base de datos por lo que ya no nos tenemos que preocupar en colocar la fecha 
    # db_column > indicar como se tiene que llamar esta columna en la base de datos solamente si queremos cambiar el nombre del atributo
    fechaCreacion = models.DateTimeField(auto_now_add=True, db_column='fecha_creacion')
    # Forma de indicar que accion debe tomar cuando se elimine el 'padre'
    # https://docs.djangoproject.com/en/4.1/ref/models/fields/#django.db.models.ForeignKey.on_delete
    # CASCADE > Cuando se elimine una categoria en forma de cascada se eliminaran todos los platos
    # PROTECT > Evita la eliminacion de la categoria si esta tiene platos que dependan de ella, emitira un error ProtectedError
    # RESTRICT > Restinge la eliminacion, es lo mismo que el PROTECT solo que emitira un error de tipo RestrictedError
    # SET_NULL > permite la eliminacion de la categoria y a los platos que dependan de ella les cambiar su valor por NULL
    # SET_DEFAULT > permite la eliminacion de la categoria y les cambiar el valor a un valor por defecto
    # DO_NOTHING > permite la eliminacion PERO no hace nada osea mantiene el mismo numero de categoria en el plato a pesar que este no exista generando un problema de integridad 

    #related_name> sirve para acceder a todos los registros desde la otra unidad , es decir desde categoria poder acceder a todos sus platos, si es que no se define su valor sera puesto por django con el nombre de la clase TODO en minusculas seguido de la palabra _set 'platomodel_set'
    categoria = models.ForeignKey(to=CategoriaModel, on_delete=models.PROTECT, db_column='categoria_id', related_name='platos')
    
    class Meta:
        db_table = 'platos'

#como vamos a modificar el comportamiento de l atabla auth_user de django entonces tenemos que modificar su herencia
class UsuarioModel(AbstractBaseUser):
    #https://docs.djangoproject.com/en/4.1/topics/auth/customizing/
    #AbstractBaseUser> me permite modificar todo lo qe yo quiera del modelo auth_user mientras que AbstracUser solamnente me permite agrgarr nuevas columnas
    id=models.AutoField(primary_key=True, unique=True)
    nombre= models.CharField(mas_lenght=50, null=False)
    apellido= models.CharField(mas_lenght=50, null=False)
    #django hace una validacion para que el correo cumpla con el formato valido
    #XXXXX@XXXX.XXX
    correo= models.EmailField(mas_lenght=100, unique=True, null=False)
    password=models.TextField(null=False)
    #Choices (opciones)> porque el primero es con el se guardara en la barra de datos
    #el segundo es con el que se mostrara al momento de devolver la informacion
    tipoUsuario=models.CharField(max_length=40, choices=[
        ('ADMIN', 'ADMINISTRADOR'),
        ('MOZO', 'MOZO')
        #('CLIENTE', 'CLIENTE')
    ])
    #propiedades netas para el panel administartivo
    #sirve para inidicar si el usuario que quiere acceder pertenece o no al equipo de trabajo
    is_staff= models.BooleanField(default=True) 
    #sirve para indicar si el usuario es un usuario activo de la empresa
    is_active=models.BooleanField(default=True) 
    #sirve para indicar la fecha en la que se creo el ususario
    createdAt=models.DateField(auto_now_add=True, db_column='created_at')
    #para el epanle admisnitrativo para indicar cual es el atributo que debe pedir como nombre de ususario
    USERNAME_FIELD='correo' 

    REQUIRED_FIELDS=['nombre','apellido', 'tipoUsuario'] 

    objects= UsuarioManager()

    class Meta:
        db_table = 'usuarios'

