import pika
import json
import os
from main import Product, db
from dotenv import load_dotenv
load_dotenv()

RABBITMQ_URL = str(os.getenv('RABBITMQ_URL'))
params = pika.URLParameters(RABBITMQ_URL)
connection = pika.BlockingConnection(params)
channel = connection.channel()
channel.queue_declare(queue='flask')


def insert_product(app, data):
    with app.app_context():
        product = Product(id=data['id'], name=data['name'], quantity=data['quantity'])
        db.session.add(product)
        db.session.commit()
        print('Product Created')


def callback(ch, method, properties, body):
    print('Received in flask')
    data = json.loads(body)
    print(data)

    if properties.content_type == 'product_created':
        product = Product(id=data['id'], name=data['name'], quantity=data['quantity'])
        db.session.add(product)
        db.session.commit()
        print('Product Created')

    elif properties.content_type == 'product_updated':
        product = Product.query.get(data['id'])
        product.name = data['name']
        product.quantity = data['quantity']
        db.session.commit()
        print('Product Updated')

    elif properties.content_type == 'product_deleted':
        product = Product.query.get(data)
        db.session.delete(product)
        db.session.commit()
        print('Product Deleted')


channel.basic_consume(queue='flask', on_message_callback=callback, auto_ack=True)
print('Started Consuming')
channel.start_consuming()
channel.close()
