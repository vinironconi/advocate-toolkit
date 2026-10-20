from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return "Bem vindo ao aplicativo para consultores de bem-estar!"  

@app.route('/about')
def about():
    return "Este é um aplicativo para consultores de bem-estar, projetado para ajudá-los a gerenciar suas atividades e interações com os clientes de forma eficiente."