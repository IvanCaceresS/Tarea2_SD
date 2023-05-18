# Sistemas_Dristribuidos_T2

# -----------------------KAFKA------------------------------
# Levantar sistema
docker compose up --build 
# Botar sistema
docker compose down -v

#Abrir la bash de cada contener creado
docker ps
docker exec -it <id_contenedor> bash
docker exec -it producer bash
docker exec -it consumer bash


# PROBANDO SI FUNCIONA KAFKA
LISTAMOS LOS TOPICS EXISTENTES:
- kafka-topics.sh --list --bootstrap-server localhost:9092
Enviamos mensajes desde un producer:
- kafka-console-producer.sh --broker-list localhost:9092 --topic mi_tema
Leemos los mensajes desde un consumer:
- kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic mi_tema --from-beginning

# -----------------------------------------------------------