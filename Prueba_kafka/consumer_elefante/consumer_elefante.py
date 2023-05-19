from kafka import KafkaConsumer
import json
import random

def consume_messages(topic_name):
    consumer = KafkaConsumer(topic_name, bootstrap_servers=['kafka:9092'], value_deserializer=lambda x: json.loads(x.decode('utf-8')))
    for message in consumer:
        print(f"Mensaje recibido de {message.topic}: {message.value}")

if __name__ == "__main__":
    topic = "Elefante"
    print("Estoy escuchando el topic ", topic)
    consume_messages(topic)
