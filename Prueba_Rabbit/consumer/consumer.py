# #!/usr/bin/env python
# import pika, sys, os

# def main():
#     connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq'))
#     channel = connection.channel()

#     channel.queue_declare(queue='hello')

#     def callback(ch, method, properties, body):
#         print(" [x] Received %r" % body)

#     channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)

#     print(' [*] Waiting for messages. To exit press CTRL+C')
#     channel.start_consuming()

# if __name__ == '__main__':
#     try:
#         main()
#     except KeyboardInterrupt:
#         print('Interrupted')
#         try:
#             sys.exit(0)
#         except SystemExit:
#             os._exit(0)

import pika
import random

def consume_messages(queue):
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq'))
    channel = connection.channel()
    channel.queue_declare(queue=queue)

    def callback(ch, method, properties, body):
        print(" [x] Received %r" % body)

    channel.basic_consume(queue=queue, on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == "__main__":
    queues = ["topic_Category0", "topic_Category1", "topic_Category2", "topic_Category3", "topic_Category4"]
    queue = random.choice(queues)
    print("Estoy escuchando el topic ", queue)
    consume_messages(queue)