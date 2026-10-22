import csv


PRODUCTS_FILE = "products.csv"
PV_GOAL = 100  # minimum pv monthly
EXCHANGE_RATE = int(1300)


def load_products(filename):
    with open(filename, newline="") as file:
        products = []
        for row in csv.DictReader(file):
            row["regular"] = float(row["regular"])
            row["membros"] = float(row["membros"])
            row["pv"] = float(row["pv"])
            products.append(row)
        return products


def search_products(products, query):
    product_search = []
    query = query.strip()
    if not query:
        return product_search
    for product in products:
        if query.lower() in product["name"].lower():
            product_search.append(product)
    return product_search


def calculate_total(order, price_type="membros"):
    total_order = 0
    if price_type != "membros" and price_type != "regular":
        raise ValueError("Invalid Price Types")
    for product, quantity in order:
        total_order += product[price_type] * quantity
    return round(total_order, 2)


def to_guaranis(total_order, exchange_rate=EXCHANGE_RATE):
    total = round(total_order * exchange_rate, -3)
    return int(total)


def calculate_pv(order):
    total_pv = 0
    if not order:
        return 0
    for product, quantity in order:
        total_pv += product["pv"] * quantity
    return total_pv


def pv_remaining(total_pv, goal=PV_GOAL):
    remain = goal - total_pv
    if remain <= 0:
        return 0
    else:
        return remain


def format_price(value, currency):
    if currency == "BRL":
        return f"R$ {value:.2f}" 
    elif currency == "PYG":
        return f"Gs {to_guaranis(value):,}".replace(",", ".")
    else:
        raise ValueError("Invalid Currency")

