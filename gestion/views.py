from rest_framework.generics import ListCreateAPIView
from .models import CategoriaModel, PlatoModel
from .serializers import CategoriaSerializer, PlatoSerializer
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
        if valida==False:
            return Response (data={
            'message':'la informacion es invalida',
            #errors> mostrar los errores SOLAMENTE cuando la data no sea valida
            'content':serializador.errors
             })
        #asi guardamos la informacion en la base de datos utilizando el serializador
        nuevoPlato=serializador.save()
        print(nuevoPlato)

        return Response (data={
            'message':'Plato creado exitosamente'
        })
