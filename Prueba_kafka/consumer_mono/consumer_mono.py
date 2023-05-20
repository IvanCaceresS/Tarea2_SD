from kafka import KafkaConsumer
import json
import random
import time

def consume_messages(topic_name):
    consumer = KafkaConsumer(topic_name, bootstrap_servers=['kafka:9092'], value_deserializer=lambda x: json.loads(x.decode('utf-8')))
    with open("latency_kafka.txt", "a") as file:
        for message in consumer:
            received_timestamp = time.time()
            message_timestamp = message.value["timestamp"]
            latency = received_timestamp - message_timestamp
            file.write(f"{latency}\n")
            print(f"Mensaje recibido de {message.topic}: {message.value}, Latencia: {latency}")

if __name__ == "__main__":
    topic = "Mono"
    print("Estoy escuchando el topic ", topic)
    consume_messages(topic)
