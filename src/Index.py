from flask import Flask, render_template,request, flash, redirect,url_for, session
from types import TracebackType
import pymysql

#se crea el objeto flask
app = Flask(__name__)


#Definimos la pagina inicial
@app.route('/')

#funcion para la pagina inicial
def home():
    if 'nombre' in session:
       return render_template('home.html')
    else:
        return render_template('login.html')

#Definimos la pagina ayuda
@app.route('/ayuda')

#funciones para la pagina ayuda
def ayuda():
    return render_template('ayuda.html')
#definimos la clase base de datos

    #creamos la sentencia de coneccion con pymysql
    self.connection= pymysql.connect(
        hots='localhost', #colocamos la ip del servido en este caso esta en local host
        user='root', #nombre del usuario con el que entramos
        password='GEHgio-1012', #contraseña del usuario que pusimos antes
        db='juegoWeb' #nombre de la base de datos que conectaremos
    )
    #creamos el cursor
    self.cursor=self.connection.cursor()
#Definimos la pagina login
@app.route("/login", methods=["GET","POST"])
#funciones para la pagina login
def login():
    return render_template('login.html')
    if(request.method=="GET"):
        if 'nombre' in session:
            return render_template('home.html')
        else:
            return render_template('login.html')
    else:
        #obtenemos los datos de registro
        nombre = request.form['nmNombreRegistro']


if __name__=='__main__':
    app.run(debug=True)