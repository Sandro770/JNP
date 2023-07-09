import pika
import json
from admin.settings import RABBITMQ_URL

params = pika.URLParameters(RABBITMQ_URL)
connection = pika.BlockingConnection(params)
channel = connection.channel()
channel.queue_declare(queue='admin')


def callback(ch, method, properties, body):
    print('Received in admin')
    data = json.loads(body)

    if properties.content_type == 'product_created':
        print('Product Created')

    elif properties.content_type == 'product_updated':
        print('Product Updated')

    elif properties.content_type == 'product_deleted':
        print('Product Deleted')


channel.basic_consume(queue='admin', on_message_callback=callback, auto_ack=True)
print('Started Consuming')
channel.start_consuming()
channel.close()
