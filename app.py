from flask import Flask, render_template, request
from toolkit import load_products, search_products, calculate_total, to_guaranis, calculate_pv, pv_remaining, PV_GOAL, EXCHANGE_RATE, PRODUCTS_FILE


app = Flask(__name__)
products = load_products(PRODUCTS_FILE)

@app.route('/')
def index():
    query = request.args.get('query', '')
    products_to_show = products
    if query.strip():
        products_to_show  = search_products(products, query)
    return render_template('index.html', products=products_to_show, pv_goal=PV_GOAL, exchange_rate=EXCHANGE_RATE, query=query)

@app.route('/about')
def about():
    return "Este é um aplicativo para consultores de bem-estar, projetado para ajudá-los a gerenciar suas atividades e interações com os clientes de forma eficiente."