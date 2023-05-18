import pika
import json

rabbitmq_host = 'localhost'
queue = 'test_queue'

def process_message(channel, method, properties, body):
    data = json.loads(body.decode('utf-8'))
    print(f"Received message: {data}")
    channel.basic_ack(delivery_tag=method.delivery_tag)

connection = pika.Blocking
