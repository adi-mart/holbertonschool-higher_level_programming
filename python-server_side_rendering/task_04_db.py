#!/usr/bin/python3
""" Flask application to display data from JSON, CSV files or SQL database. """
from flask import Flask, render_template, request
import json
import csv
import sqlite3

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


def read_sql_database():
    """Read and return data from SQL database"""
    try:
        conn = sqlite3.connect('products.db')
        cursor = conn.cursor()
        # Exécuter la requête SQL
        cursor.execute('SELECT id, name, category, price FROM Products')
        # Récupérer tous les résultats
        rows = cursor.fetchall()
        # Convertir les résultats en liste de dictionnaires
        products = []
        for row in rows:
            products.append({
                'id': row[0],
                'name': row[1],
                'category': row[2],
                'price': row[3]
            })

        conn.close()
        return products

    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return None


@app.route('/products')
def products():
    # Récupérer les paramètres de requête
    source = request.args.get('source')
    product_id = request.args.get('id')

    # Vérifier que le paramètre source est valide
    if source not in ['json', 'csv', 'sql']:
        return render_template('product_display.html', error="Wrong source")

    # Lire les données selon la source
    if source == 'json':
        products_data = read_json_file()
    elif source == 'csv':
        products_data = read_csv_file()
    else:  # sql
        products_data = read_sql_database()

    # Vérifier si les données ont été lues correctement
    if products_data is None:
        return render_template(
          'product_display.html', error="Error reading data source")

    # Si la liste est vide
    if not products_data:
        return render_template(
          'product_display.html', error="No products found in database")

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
