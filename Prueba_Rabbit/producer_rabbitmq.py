import time
import json
import pika

rabbitmq_host = 'localhost'
queue = 'test_queue'

connection = pika.BlockingConnection(pika.ConnectionParameters(host=rabbitmq_host))
channel = connection.channel()
channel.queue_declare(queue=queue)

while True:
    timestamp = int(time.time())
    message = {
        'timestamp': timestamp,
        'message': 'Hello, RabbitMQ!'
    }
    channel.basic_publish(exchange='', routing_key=queue, body=json.dumps(message))
    print(f"Sent message: {message}")

    time.sleep(1)

connection.close()
