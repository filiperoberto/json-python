from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

from json_file_appender import *
from json_file_loader import *

file = "test_original.json"

# Este é o arquivo com as rotas para o navegador interagir

#/api vai entregar a página html para o navegador

@app.route("/api") 
def index():
    return render_template('api.html')

#/ vai ler o json e entregar para o navegador

@app.route("/")
def ler():
    return deconstruction_var_json(file)

#/ vai pegar o json do navegador e escrever no json, note que este é um método post, quer dizer que ele recebe dados do navegador

@app.route("/", methods = ["POST"])
def escrever():
    write_json(request.get_json(), file)
    return request.get_json()