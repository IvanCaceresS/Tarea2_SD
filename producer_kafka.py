import time
import json
import random
from kafka import KafkaProducer

def generate_message(device_id, device_name, category, message_size):
    timestamp = time.time()
    values = ''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=message_size))
    message = {"timestamp": timestamp, "value": {"data": values}}
    return json.dumps(message)

def produce_messages(num_devices, delta_t, min_message_size, max_message_size):
    producer = KafkaProducer(bootstrap_servers='localhost:9092', value_serializer=lambda v: str(v).encode('utf-8'))

    devices = [
        {"id": i, "name": f"Device{i}", "category": f"Category{i % 5}"}  # Assigning categories to devices
        for i in range(num_devices)
    ]

    while True:
        for device in devices:
            message_size = random.randint(min_message_size, max_message_size)
            message = generate_message(device["id"], device["name"], device["category"], message_size)
            if device["category"] == "Category0":
                topic_name = "topic_Category0"
            elif device["category"] == "Category1":
                topic_name = "topic_Category1"
            elif device["category"] == "Category2":
                topic_name = "topic_Category2"
            elif device["category"] == "Category3":
                topic_name = "topic_Category3"
            elif device["category"] == "Category4":
                topic_name = "topic_Category4"
            else:
                topic_name = "default_topic"  # Default topic if no category matches
                
            producer.send(topic_name, value=message)
            print(f"Device {device['id']}, {topic_name}, sending: {message}")
        
        time.sleep(delta_t)

if __name__ == "__main__":
    num_devices = 3  # Number of IoT devices
    delta_t = 1  # Time interval between message sends (in seconds)
    min_message_size = 10  # Minimum size of the information sent by each device
    max_message_size = 20  # Maximum size of the information sent by each device

    produce_messages(num_devices, delta_t, min_message_size, max_message_size)
