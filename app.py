from flask import Flask, redirect, render_template, request, session
from toolkit import load_products, search_products, calculate_total, to_guaranis, calculate_pv, pv_remaining, format_price, PV_GOAL, EXCHANGE_RATE, PRODUCTS_FILE


app = Flask(__name__)
app.secret_key = "55dd0a6db3fac20e894d41cc59d16232"  # Replace with a secure secret key in production
app.add_template_filter(format_price, "format_price")
products = load_products(PRODUCTS_FILE)

@app.route("/")
def index():
    query = request.args.get("query", "")
    currency = session.get("currency", "BRL")  # Default to BRL if not set
    products_to_show = products
    if query.strip():
        products_to_show  = search_products(products, query)
    return render_template("index.html", products=products_to_show, pv_goal=PV_GOAL, exchange_rate=EXCHANGE_RATE, query=query, currency=currency)

@app.route("/about")
def about():
    return "Este é um aplicativo para consultores de bem-estar, projetado para ajudá-los a gerenciar suas atividades e interações com os clientes de forma eficiente."

@app.route("/currency", methods=["POST"])
def set_currency():
    currency = request.form.get("currency")
    if currency in ["BRL", "PYG"]:
        session["currency"] = currency
    return redirect("/")