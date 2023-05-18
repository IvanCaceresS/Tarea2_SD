# Sistemas_Dristribuidos_T2
pip install kafka-python

docker-compose -f docker-compose-kafka.yml up -d



# PROBANDO SI FUNCIONA KAFKA

kafka-topics.sh --create --topic mi_tema --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1



LISTAMOS LOS TOPICS EXISTENTES:
- kafka-topics.sh --list --bootstrap-server localhost:9092
Enviamos mensajes desde un producer:
- kafka-console-producer.sh --broker-list localhost:9092 --topic mi_tema
Leemos los mensajes desde un consumer:
- kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic mi_tema --from-beginning
