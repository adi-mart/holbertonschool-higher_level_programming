#!/usr/bin/python3
""" Flask application with multiple routes and Jinja templates. """

from flask import Flask, render_template
import json

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/items')
def items():
    # Lire le fichier JSON
    with open('items.json', 'r') as file:
        data = json.load(file)

    # Extraire la liste des items
    items_list = data.get('items', [])

    # Passer la liste au template
    return render_template('items.html', items=items_list)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
