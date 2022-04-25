from flask import Flask, render_template, abort, request
from funciones import *
import os

app = Flask(__name__)

datos=Leer_Json("books.json")

@app.route('/')
def inicio():
    return render_template("index.html",datos=datos)

@app.route('/libro/<isbn>')
def libro(isbn):
    for libro in datos:
        if libro.get("isbn") == isbn:
            return render_template("libro.html", libro=libro)
    return abort(404)

@app.route('/categorias/<categoria>')
def categorias(categoria):
    return render_template("categorias.html", datos=datos, categoria=categoria)

port=os.environ["PORT"]
app.run('0.0.0.0',int(port), debug=False)
