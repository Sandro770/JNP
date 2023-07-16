import requests
from flask import Flask, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from sqlalchemy import UniqueConstraint
from dataclasses import dataclass
from producer import publish


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


@dataclass
class ProductUser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    product_id = db.Column(db.Integer)

    UniqueConstraint('user_id', 'product_id', name='user_product_unique')


@app.route('/api/products')
def index():
    return jsonify(Product.query.all())


@app.route('/api/products/<int:id>/buy', methods=['POST'])
def buy(id):
    pass  # to fix


@app.route('/api/products/<int:id>/like', methods=['POST'])
def like(id):
    # req = requests.get('http://localhost:8000/api/user')
    # json = req.json()
    
    # try:
    #     productUser = ProductUser(user_id=json['id'], product_id=id)
    #     db.session.add(productUser)
    #     db.session.commit()
        
    publish('product_liked', id)
    # except:
    #     abort(400, 'You already liked this prodcut')

    return jsonify({
        'message': 'success'
    })


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
