import time
import json
import random
from kafka import KafkaProducer

def generate_message(message_size):
    timestamp = time.time()
    values = ''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=message_size))
    message = {"timestamp": timestamp, "value": {"data": values}}
    return json.dumps(message)

def produce_messages(random_topic, delta_t, min_message_size, max_message_size):
    producer = KafkaProducer(bootstrap_servers='kafka:9092', value_serializer=lambda v: str(v).encode('utf-8'))

    while True:
            message_size = random.randint(min_message_size, max_message_size)
            message = generate_message(message_size)
                           
            producer.send(random_topic, value=message)
            print(f"{random_topic}, sending: {message}")
        
            time.sleep(delta_t)

if __name__ == "__main__":
    delta_t = 1  # Time interval between message sends (in seconds)
    min_message_size = 10  # Minimum size of the information sent by each device
    max_message_size = 20  # Maximum size of the information sent by each device

    produce_messages("Leon", delta_t, min_message_size, max_message_size)