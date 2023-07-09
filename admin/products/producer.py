import pika
import json
import os
from dotenv import load_dotenv
load_dotenv()

RABBITMQ_URL = str(os.getenv('RABBITMQ_URL'))
params = pika.URLParameters(RABBITMQ_URL)
connection = pika.BlockingConnection(params)
channel = connection.channel()


def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='admin', body=json.dumps(body), properties=properties)
