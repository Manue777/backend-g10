from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from models.categorias_model import Categoria

class CategoriaDto(SQLAlchemyAutoSchema):
    class Meta:
        model=Categoria
    #sirve para pasarle los metadatos a la claseque estamos heredando es una clase  exclusiva de python
    #metdatos osn informacion que necesita la clase que estamos haciendo
    #como atributos para que pueda funcionar correctamente
    #sirve para inidcar medinate que modelo se tiene que guiar para hacer el mapeo  de la informacion
    
