# from kafka import KafkaConsumer
# import json

# def consume_messages(topic_name):
#     consumer = KafkaConsumer(topic_name, bootstrap_servers=['kafka:9092'], value_deserializer=lambda x: json.loads(x.decode('utf-8')))
#     for message in consumer:
#         print(f"Mensaje recibido de {message.topic}: {message.value}")

# if __name__ == "__main__":
#     topic_names = ["topic_Category0","topic_Category1","topic_Category2","topic_Category3","topic_Category4"]
#     consume_messages(topic_name)

from kafka import KafkaConsumer
import json
import random

def consume_messages(topic_name):
    consumer = KafkaConsumer(topic_name, bootstrap_servers=['kafka:9092'], value_deserializer=lambda x: json.loads(x.decode('utf-8')))
    for message in consumer:
        print(f"Mensaje recibido de {message.topic}: {message.value}")

if __name__ == "__main__":
    topic_names = ["topic_Category0", "topic_Category1", "topic_Category2", "topic_Category3", "topic_Category4"]
    random_topic = random.choice(topic_names)
    print("Estoy escuchando el topic ", random_topic)
    consume_messages(random_topic)
