from rest_framework.generics import ListCreateAPIView, DestroyAPIView, ListAPIView
from .models import CategoriaModel, PlatoModel
from .serializers import CategoriaSerializer, PlatoSerializer,CategoriaConPlatosSerializer
from rest_framework.response import Response
from rest_framework.request import Request

# List > Listar (get)
# Create > Crear (post)

class CategoriaApiView(ListCreateAPIView):
    # al utilizar una vista generica que ya no es necesario definir el comportamiento para cuando sea get o post
    # queryset > el comando que utilizara para llamar a la informacion de nuestra base de datos
    # SELECT * FROM categoria;
    queryset = CategoriaModel.objects.all()
    # serializer_class > se define una clase que se encargara de convertir y transformar la informacion que viene desde el cliente y la informacion que enviamos hacia el cliente en dato legibles

    serializer_class = CategoriaSerializer
    # ya no es necesario definir los metodos 'get' y 'post'
    # def get(self):
    #     pass

    # def post(self):
    #     pass

class PlatoApiView(ListCreateAPIView):
    queryset = PlatoModel.objects.all()
    serializer_class= PlatoSerializer

    def get(self, request: Request):
        #al colocar':' inidcamos que el tipo de dato que sera esa variable en el caso que no la hemos setteado correctamente
        #request> toda la informacion que viene del cliente
        #SELECT*FROM platos WHERE disponibilidad= true;
        resultado=PlatoModel.objects.filter(disponibilidad=True).all()
        print (resultado)
        #aca llamamos al serilizer y le pasamos la informacion proveniniente de la bd y con el parametro many True indicamos que le estamos pasando un arreglo de instancias
        serializador=PlatoSerializer(instance=resultado, many=True)
        print(serializador.data)

        return Response (data={
            'content':serializador.data
        })
    
    def post (self, request:Request):
        body=request.data
        #cuando queremos verificar si la informacion entrante es validad entonces utilizamos el parametro data en vez del parametro instance
        serializador=PlatoSerializer(data=body)
        #es el encargado de validar si la data es correcta y cumple con todos los requisitos
        valida= serializador.is_valid()

        #SELECT*FROM platos WHERE nombre= '...'LIMT 1;
        platoExistente=PlatoModel.objects.filter (nombre= body.get('nombre')).first()

        if platoExistente:
            return Response (data={
                'message':'El plato con nombre {} ya existe'.format(platoExistente.nombre)
            })

      
        if valida==False:
            return Response (data={
            'message':'la informacion es invalida',
            #errors> mostrar los errores SOLAMENTE cuando la data no sea valida
            'content':serializador.errors
            })
        
        #si la data pasada al serializador es una data valida entonces esta informacion se guardara en el validated_data que es un diccionario, el validate_data solamente estara disponible cuando mandemos a la validacion, si no se hace la validacion el validate_data sera vacio
        # platoExistente=PlatoModel.objects.filter (nombre=serializador.validated_data.get('nombre')).first()
        # if platoExistente:
        #     return Response (data={
        #     'message':'el plato con nombre{} ya existe'.format(platoExistente.nombre)
        #     })
        
        #asi guardamos la informacion en la base de datos utilizando el serializador
        print(serializador.validated_data)

        nuevoPlato=serializador.save()
        print(nuevoPlato)

        serializar = PlatoSerializer(instance=nuevoPlato)
        return Response (data={
            'message':'Plato creado exitosamente',
            #data> es la informacion convertida a un diccionario para que pueda ser entendido pr el cliente
            'content':serializar.data
        })
    
class PlatoDestroyAPIView(DestroyAPIView):
    #queryset=PlatoModel.objects.all()
    #serializer_class=PlatoSerializer

    def delete (self, request:Request, pk:int):
        print(pk)
        platoEncontrado=PlatoModel.objects.filter(id=pk, disponibilidad=True).first()
        if platoEncontrado is None:
            return Response (data={
            'message':'El plato no existe'
        })
        #Le canbiamos la disponibilidad
        platoEncontrado.disponibilidad=False
        #guardamos los cambios en la bd
        platoEncontrado.save()

        return Response (data={
            'message':'Plato eliminado exitosamente'
        })
    
class ListarCategoriaApiView(ListAPIView):
    def get (self, request:Request, pk:int):
        categoriaEncontrada= CategoriaModel.objects.filter(id=pk).first()
        print(categoriaEncontrada)

        if categoriaEncontrada is None:
            return Response (data={
                'message':'Categoria no existe'
            })
        serializador = CategoriaConPlatosSerializer(instance=categoriaEncontrada)

        return Response (data={
            'content':'serializador.data'
        })
    

