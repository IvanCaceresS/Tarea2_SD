import pika
import time
import random
import json

def consume_messages(queue):
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq'))
    channel = connection.channel()
    channel.queue_declare(queue=queue)

    # Crear o abrir el archivo de texto para almacenar las latencias
    with open('latencias.txt', 'a') as file:

        def callback(ch, method, properties, body):
            message = json.loads(body.decode())
            received_timestamp = time.time()
            sent_timestamp = message['timestamp']
            latency = received_timestamp - sent_timestamp

            print(f"Mensaje recibido de {queue}: {body}")
            print(f"Latencia: {latency} segundos")

            # Almacenar la latencia en el archivo de texto
            file.write(f"{latency}\n")

        channel.basic_consume(queue=queue, on_message_callback=callback, auto_ack=True)

        print(' [*] Waiting for messages. To exit press CTRL+C')
        channel.start_consuming()


if __name__ == "__main__":
    queue = "Leon"
    print("Estoy escuchando el topic ", queue)
    consume_messages(queue)
