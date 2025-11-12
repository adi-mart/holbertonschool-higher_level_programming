#!/usr/bin/python3
""" Flask application to display data from JSON or CSV files. """
from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)


def read_json_file():
    """read and return data from JSON file"""
    try:
        with open('products.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return None


def read_csv_file():
    """read and return data from CSV file"""
    try:
        products = []
        with open('products.csv', 'r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                # Convertir l'id en int et le price en float
                products.append({
                    'id': int(row['id']),
                    'name': row['name'],
                    'category': row['category'],
                    'price': float(row['price'])
                })
        return products
    except FileNotFoundError:
        return None


@app.route('/products')
def products():
    # Récupérer les paramètres de requête
    source = request.args.get('source')
    product_id = request.args.get('id')

    # Vérifier que le paramètre source est valide
    if source not in ['json', 'csv']:
        return render_template('product_display.html', error="Wrong source")

    # Lire les données selon la source
    if source == 'json':
        products_data = read_json_file()
    else:  # csv
        products_data = read_csv_file()

    # Vérifier si les données ont été lues correctement
    if products_data is None:
        return render_template(
          'product_display.html', error="Error reading file")

    # Filtrer par ID si fourni
    if product_id:
        try:
            product_id = int(product_id)
            filtered_products = [
                p for p in products_data if p['id'] == product_id
            ]

            if not filtered_products:
                return render_template(
                  'product_display.html', error="Product not found")

            products_data = filtered_products
        except ValueError:
            return render_template(
              'product_display.html', error="Invalid product ID")

    # Afficher les produits
    return render_template('product_display.html', products=products_data)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
