import time
import json
import pika
import random

def generate_messages():
    messages = []
    
    with open('./datos_livianos.txt', 'r') as file:
        for line in file:
            data = line.strip()  # Lee y elimina los espacios en blanco alrededor de cada línea
            message = data
            messages.append(json.dumps(message))
    
    return messages

def produce_messages(queue, delta_t,messages):
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq'))
    channel = connection.channel()

    for i in range(len(messages)):     
            timestamp = time.time()
            message = {"timestamp": timestamp, "value": {"data": json.loads(messages[i])}}
            msg = json.dumps(message)
            channel.basic_publish(exchange='', routing_key=queue, body=msg)
            print(f"{queue}, sending: {msg}")
            time.sleep(delta_t)
        

if __name__ == "__main__":
    delta_t = 1  # Time interval between message sends (in seconds)
    messages = generate_messages()
    produce_messages("Elefante", delta_t, messages)