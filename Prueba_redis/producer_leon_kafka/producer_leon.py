import time
import json
import random
from kafka import KafkaProducer


def generate_messages():
    messages = []
    
    with open('./datos.txt', 'r') as file:
        for line in file:
            data = line.strip()  # Lee y elimina los espacios en blanco alrededor de cada línea
            
            timestamp = time.time()
            message = {"timestamp": timestamp, "value": {"data": data}}
            messages.append(json.dumps(message))
    
    return messages

def produce_messages(random_topic, delta_t, messages):
    producer = KafkaProducer(bootstrap_servers='kafka:9092', value_serializer=lambda v: str(v).encode('utf-8'))
    
    for i in range(len(messages)):
        producer.send(random_topic, value=messages[i])
        print(f"{random_topic}, sending: {messages[i]}")
        time.sleep(delta_t)


if __name__ == "__main__":
    delta_t = 1  # Time interval between message sends (in seconds)
    messages = generate_messages()
    produce_messages("Leon", delta_t, messages)