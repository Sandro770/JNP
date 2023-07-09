import requests
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from sqlalchemy import UniqueConstraint
from dataclasses import dataclass


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
CORS(app)
db = SQLAlchemy(app)

app.app_context().push()


@dataclass
class Product(db.Model):
    id: int
    name: str
    quantity: int

    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    name = db.Column(db.String(200))
    quantity = db.Column(db.Integer)


class ProductUser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    product_id = db.Column(db.Integer)

    UniqueConstraint('user_id', 'product_id', name='user_product_unique')


@app.route('/api/products')
def index():
    return jsonify(Product.query.all())


@app.route('/api/products/<int:pk>/buy', methods=['POST'])
def buy(id):
    pass


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
