# from kafka import KafkaConsumer

# servidores_bootstrap = 'kafka:9092'
# topic = 'mi_tema'

# consumidor = KafkaConsumer(topic, bootstrap_servers=[servidores_bootstrap])

# for msg in consumidor:
#     print(msg.value)

from kafka import KafkaConsumer
import json

def consume_messages(topic_name):
    consumer = KafkaConsumer(topic_name, bootstrap_servers=['kafka:9092'], value_deserializer=lambda x: json.loads(x.decode('utf-8')))
    for message in consumer:
        print(f"Mensaje recibido de {message.topic}: {message.value}")

if __name__ == "__main__":
    topic_name = "topic_Category0"  # Nombre del topic a consumir
    consume_messages(topic_name)
