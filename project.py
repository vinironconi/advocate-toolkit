"""
This is an advocate toolkit for essential oils advocate
Not Affiliated or endorsed by Doterra

"""

import csv
import sys
from tabulate import tabulate
from toolkit import load_products, search_products, calculate_total, to_guaranis, calculate_pv, pv_remaining, PV_GOAL, EXCHANGE_RATE, PRODUCTS_FILE



def main():
    products = load_products(PRODUCTS_FILE)
    order = []  # list of products/quantity
    currency = get_currency()

    while True:
        print("\n=== Advocate Toolkit ===")
        print("1. Search products")
        print("2. Add product to order")
        print("3. View Order")
        print("4. Change Currency")
        print("5. Quit")
        choice = input("> ").strip()

        if choice == "1":
            query = input("Search: ")
            show_products(search_products(products, query), currency)
        elif choice == "2":
            add_to_order(products, order, currency)
        elif choice == "3":
            show_order(order, currency)
        elif choice == "4":
            currency = get_currency()
        elif choice == "5":
            sys.exit("Goodbye")

def get_currency():
    while True:
        print("\n=== Choose currency ===")
        print("1. Reais")
        print("2. Guaranis")
        currency = input("> ").strip()
        if currency == "1" or currency == "2":
            return currency
        else:
            print("Not valid")



def add_to_order(products, order, currency):
    query = input("Product: ")
    matches = search_products(products, query)
    if not matches:
        print("Could not find Product")
        return
    if len(matches) > 1:
        show_products(matches, currency)
        print("Please be more specific")
        return
    product = matches[0]
    while True:
        try:
            quantity = int(input("How many would you like to add? "))
            if quantity > 0:
                break
            else:
                print("Number must be positive")
        except ValueError:
            print("Please type a number")
    order.append((product, quantity))
    print(f"Added {quantity} x {product['name']}")



def show_products(products, currency):
    if not products:
        print("No products found.")
        return
    if currency == "1":
        rows = [
            [
                p["name"],
                p["size"],
                f"R${p['membros']:.2f}",
                f"R${p['regular']:.2f}",
                p["pv"],
            ]
            for p in products
        ]
        print(tabulate(rows, headers=["Product", "Size", "Membros", "Regular", "PV"]))
    elif currency == "2":
        rows = [
            [
                p["name"],
                p["size"],
                f"Gs{to_guaranis(p['membros']):,}".replace(",", "."),
                f"Gs{to_guaranis(p['regular']):,}".replace(",", "."),
                p["pv"],
            ]
            for p in products
        ]
        print(tabulate(rows, headers=["Product", "Size", "Membros", "Regular", "PV"]))



def show_order(order, currency):
    if not order:
        print("Your order is empty")
        return
    rows = []
    if currency == "1":
        for product, quantity in order:
            row = [
                product["name"],
                product["size"],
                quantity,
                f"R${product['membros'] * quantity:.2f}",
                product["pv"] * quantity,
            ]
            rows.append(row)
    if currency == "2":
        for product, quantity in order:
            row = [
                product["name"],
                product["size"],
                quantity,
                f"Gs{to_guaranis(product['membros'] * quantity):,}".replace(",", "."),
                product["pv"] * quantity,
            ]
            rows.append(row)

    print(tabulate(rows, headers=["Produ ct", "Size", "Quantity", "Price", "PV"]))

    total = calculate_total(order)
    if currency == "1":
        print(f"Your total is R${total:.2f}")
    if currency == "2":
        print(f"Your total is Gs{to_guaranis(total):,}".replace(",", "."))

    total_pv = calculate_pv(order)
    remaining = pv_remaining(total_pv)
    print(f"Your total pv is {total_pv:g}")
    if remaining <= 0:
        print("Pv goal reached!")
    else:
        print(f"You still have {remaining:g} pvs left to achieve {PV_GOAL} pv goal")



if __name__ == "__main__":
    main()
