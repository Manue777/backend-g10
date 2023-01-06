from flask import Flask, request
from flask_mysqldb import MySQL
from os import environ

from dotenv import load_dotenv
load_dotenv()

app = Flask (__name__)
#cuando tenemos un diccionario poder obtener el valor de una de sus llaves con el metodo obtener , no para asignar . Y si que al obtener no hay valor entonces colocara none
#esto no se peude hacer
#environ.get (MySQL_HOST)="hola"
#environ(MySQL_HOST)="hola"

app.config['MYSQL_HOST'] = environ.get('MYSQL_HOST')
app.config['MYSQL_USER'] = environ.get('MYSQL_USER')
app.config['MYSQL_PASSWORD'] = environ.get('MYSQL_PASSWORD')
app.config['MYSQL_DB'] = environ.get('MYSQL_DB')
app.config['MYSQL_PORT'] = int(environ.get('MYSQL_PORT'))

#inicialiazmoa la conexion setenado los parametros
mysql = MySQL(app)

@app.route("/productos", methods= ["GET", "POST"])
def gestion_productos():
    if request.method == "GET":
        #crea una conexion a la base de datos mediante un cursor
        cursor=mysql.connection.cursor()
        cursor.execute("SELECT * FROM productos")
        productos =cursor.fetchall()  #limt infinito
        #cursor
        print(productos)
        #cerrar nuestra conexion
        cursor.close()
        return{
            "message": "los productos son"
        }
    elif request.method == "POST":
        return{
            "message": "productos creados exitosamente"
        }  
     
#load_dotenv > cargamos todas las variables definidas en el archivo .env
app.run(debug=True)

