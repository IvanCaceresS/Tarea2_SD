# #!/usr/bin/env python
# import pika
# import random

# connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq'))
# channel = connection.channel()
# queues = ["topic_Category0", "topic_Category1", "topic_Category2", "topic_Category3", "topic_Category4"]

# queue = random.choice(queues)
# channel.queue_declare(queue='queue')

# channel.basic_publish(exchange='', routing_key='queue', body='Hello World!')
# print(" [x] Sent 'Hello World!'")
# connection.close()

import time
import json
import pika
import random

def generate_message(message_size):
    timestamp = time.time()
    values = ''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=message_size))
    message = {"timestamp": timestamp, "value": {"data": values}}
    return json.dumps(message)

def produce_messages(queue, delta_t, min_message_size, max_message_size):
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq'))
    channel = connection.channel()

    while True:
            message_size = random.randint(min_message_size, max_message_size)
            message = generate_message(message_size)           
            channel.basic_publish(exchange='', routing_key=queue, body=message)
            print(f"{queue}, sending: {message}")
            time.sleep(delta_t)

if __name__ == "__main__":
    queues = ["topic_Category0", "topic_Category1", "topic_Category2", "topic_Category3", "topic_Category4"]
    queue = random.choice(queues)
    delta_t = 5  # Time interval between message sends (in seconds)
    min_message_size = 10  # Minimum size of the information sent by each device
    max_message_size = 20  # Maximum size of the information sent by each device

    produce_messages(queue, delta_t, min_message_size, max_message_size)