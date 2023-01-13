from flask_restful import Resource, request
from configuracion import conexion
from models.categorias_model import Categoria
from dtos.categoria_dto import CategoriaDto
from sqlalchemy.exc import IntegrityError
from marshmallow.exceptions import ValidationError


class CategoriasController(Resource):
    def get (self):
        #SELECT* FROM Categorias,
        data=conexion.session.query(Categoria).all()
        print(data[0].nombre)
        serializador = CategoriaDto(many=True)
        resultado= serializador.dump(data)
        return {
        
            'content':resultado
        }

    def post (self):
        data= request.get_json()
        print(data)
        serializador =CategoriaDto()
        try:
        #load> valida el diccionario que cumpla con todas las caracteristicas de las columnas de 
        #nuestro modelo y si es devolvera un diccionario con la informacion necesaria
        #raise exception('bla')
            resultado=serializador.load(data)
            print(resultado)

            nuevaCategoria=Categoria(nombre = resultado.get('nombre'))

            conexion.session.add(nuevaCategoria)
            conexion .session.commit()


            return {
                    'message':'categoria creada exitosamente'
            }

        except IntegrityError as error_integridad:
            #aca se ingresa si al momento de guradra la categoria , esta ya existe
             return {
                'message':'error al crear la categoria, esa categoria ya existe'
            }
        except ValidationError as error_validacion:
             return {
                'message':'error al crear la categoria, vea el content',
                'content': error_validacion.args
            }

        except Exception as error:
             return {
                'message':'error al crear la categoria',
                'content': error.args
            }

class CategoriaController(Resource):
    def get (self, id):
        print(id)
        #select*from categorias where id = ....limit 1
        #first > no me devuelve una lista (arreglo) sino me devuelve solo una instancia
        #all> me devuelve una lista con todas las coincidencias
        categoria=conexion.session.query(Categoria).filter_by(id= id).first()
        print(categoria)

        #Todos: convertir esta categoria para mostrar en ele content , si es que la categoria no existe (None) indicar que la categoria no existe en el mensaje
        return{
            'content': ''
        }