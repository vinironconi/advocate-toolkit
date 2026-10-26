from flask import Flask, redirect, render_template, request, session
from toolkit import load_products, search_products, calculate_total, to_guaranis, calculate_pv, pv_remaining, format_price, get_product_by_sku, PV_GOAL, EXCHANGE_RATE, PRODUCTS_FILE
import os


app = Flask(__name__)
secret_key = os.environ.get("SECRET_KEY")
if not secret_key:
    raise ValueError("SECRET_KEY environment variable is not set.")
app.secret_key = secret_key
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
    return redirect(request.referrer or "/")

@app.route("/add_to_cart", methods=["POST"])
def add_to_cart():
    sku = request.form.get("sku")
    found_product = get_product_by_sku(products, sku)
    try:
        quantity = int(request.form.get("quantity", 1))
        if quantity < 1:
            raise ValueError("Quantity must be at least 1")
    except ValueError:
        return redirect(request.referrer or "/")  # Redirect back to the main page if quantity is invalid

    if found_product:
        order = session.get("order", {})
        order[found_product["sku"]] = order.get(found_product["sku"], 0) + quantity
        session["order"] = order
    return redirect(request.referrer or "/")

@app.route("/clear_cart", methods=["POST"])
def clear_cart():
    session.pop("order", None)
    return redirect(request.referrer or "/")

@app.route("/remove_from_cart", methods=["POST"])
def remove_from_cart():
    sku = request.form.get("sku")
    found_product = get_product_by_sku(products, sku)
    try:
        quantity = int(request.form.get("quantity", 1))
        if quantity < 1:
                raise ValueError("Quantity must be at least 1")
    except ValueError:
        return redirect(request.referrer or "/")  # Redirect back to the main page if quantity is invalid
    if found_product:
        order = session.get("order", {})
        order[found_product["sku"]] = (order.get(found_product["sku"], 0) - quantity)
        if order[found_product["sku"]] <= 0:
            order.pop(found_product["sku"], None)
        session["order"] = order
    return redirect(request.referrer or "/")

@app.route("/order", methods=["GET"])    
def view_order():
    full_order = []
    order = session.get("order", {})
    for sku, quantity in order.items():
        product = get_product_by_sku(products, sku)
        if product:
            full_order.append((product, quantity))
    total_price_membros = calculate_total(full_order, price_type="membros")
    total_price_regular = calculate_total(full_order, price_type="regular")
    total_pv = calculate_pv(full_order)
    currency = session.get("currency", "BRL")  # Default to BRL if not set
    return render_template("order.html", order=full_order, total_price_membros=total_price_membros, total_price_regular=total_price_regular, total_pv=total_pv, currency=currency, pv_goal=PV_GOAL, pv_remaining=pv_remaining(total_pv, PV_GOAL))
