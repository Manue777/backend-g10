from django.db import models

class CategoriaModel(models.Model):
    #Si no especificamos la columna ID django lo hara de manera predeterminada con el tipod de dato AutoField y tbn lo colocara como llave primaria

    id= models.AutoField(primary_key=True, null=False)
    nombre= models.CharField(max_lenght=50, unique=True)

    class Meta:
        # Sirve para definir los atributos de la clse que estamos heredando directamente para pasarle la metadata sin utilisa el metodo super
        #sirve para modificar la configuracion y comrportamiento de esta tabla en la base de datos

        db_table='categorias'

        #modificamos el ordenamiento al momento de dvolver los registros 
        #nombre ascendente (a-z)
        #nombre descendete (z-a)
        #como ya sabemos que el nombre jamas se repetira la segunda clusula de ordenamiento esta de mas porque nunca se va a dar
        ordering= ['nombre','id']

class PlatoModel(models.Model):
    #id= models.AutoField(primary_key=True, null=False)
    nombre = models.CharField(max_length=50, unique=True, null=False)
    precio= models.FloatField()
    disponibilidad=models.BooleanField(default=True)
    #auto_now_add> cada vez que cree un nuevo registrp su valor sera la hora y fecha actual del srvidor de base de datos por lo que ya no nos tenemos que preocupar en colocar la fecha
    #db_columna> indicar como se tiene que llamar esta columna en la base de datos solamnete si quermeos cambiar el nombre del atributo
    fechaCreacion=models.DateTimeField(auto_now_add=True,db_column='fecha_creacion')
    #Forma de inidcar que accion debe tomar cuando se elimine el Padre
    #CASCADE>Cuando se elimina una categoria en forma de cascada se eliminaran todos los platos
    #PROTECT>Evita la eliminacion de la vategoria si esta tiene platos que dependen de ella, emitira un error ProtectError
    #SET_NULL > permite la eliminacion de la categoria y a los platos que dpenden de ella les cambia su valor por NULL
    #SET DEFAULT> permite la eliminicacion de la categoria y les cambiara el valor a un Valor por defecto
    #DO_NOTHING> permite la elmimnacion PERO no hace nada osea mantinene el mismo numero de categoria en el plato a pesar que este no exista generando un problema de integridad
    categoria=models.ForeignKey(to=CategoriaModel, on_delete=models.PROTECT, db_columna='categoria_id')








