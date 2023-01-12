from configuracion import conexion
from sqlalchemy import Column,types

class Categoria(conexion.Model):
    #estamos inidcando que esta clase se comportara ademas como si fuesa una base de datos
    #https://docs.sqlalchemy.org/en/14/core/metadata.html#sqlalchemy.schema.Column.__init__
    #https://docs.sqlalchemy.org/en/14/core/type_basics.html#generic-camelcase-types
    #id INT AUTO_INCREMENT  PRIMARY KEY
    id= Column(type_=types.Integer, autoincrement=True, primary_key=True)
    #nombre VARCHAR(45) NOT NULL UNIQUE
    nombre =Column(type_=types.String(length=45), nullable=False, unique=True)
    #inidcador como se llamara la tabla en la base de datos
    __tablename__='categorias'