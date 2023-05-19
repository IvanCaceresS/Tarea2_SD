# Sistemas_Dristribuidos_T2

# -----------------------KAFKA------------------------------
# Levantar sistema
docker compose up --build 
# Botar sistema
docker compose down -v

# Abrir la bash de cada contener creado
docker ps
docker exec -it <id_contenedor> bash (PARA ACCEDER A KAFKA CON ID CONTENEDOR DE KAFKA)
docker exec -it producer1 bash
docker exec -it producer2 bash
docker exec -it producer3 bash
docker exec -it consumer1 bash
docker exec -it consumer2 bash
docker exec -it consumer3 bash
docker exec -it consumer4 bash


# PROBANDO SI FUNCIONA KAFKA
LISTAMOS LOS TOPICS EXISTENTES:
- kafka-topics.sh --list --bootstrap-server localhost:9092
Enviamos mensajes desde un producer:
- kafka-console-producer.sh --broker-list localhost:9092 --topic mi_tema
Leemos los mensajes desde un consumer:
- kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic mi_tema --from-beginning

# -----------------------------------------------------------
# -----------------------RABBITMQ----------------------------
# Levantar sistema
docker compose up --build 
# Botar sistema
docker compose down -v

# Abrir la bash de cada contener creado
docker ps
docker exec -it <id_contenedor> bash (PARA ACCEDER A RABBITMQ CON ID CONTENEDOR DE RABBITMQ)
docker exec -it producer1 bash
docker exec -it producer1 bash
docker exec -it producer3 bash
docker exec -it consumer1 bash
docker exec -it consumer2 bash
docker exec -it consumer3 bash
docker exec -it consumer4 bash
# -----------------------------------------------------------


Escenario imaginario: Gestión de sensores ambientales en una ciudad inteligente

En el contexto de una ciudad inteligente, se desea implementar un sistema de gestión de sensores ambientales para monitorear diferentes aspectos del entorno, como la calidad del aire, la temperatura, la humedad y los niveles de ruido. El objetivo es recopilar datos de estos sensores distribuidos por toda la ciudad y enviarlos a un servidor central para su análisis y toma de decisiones.

HAY QUE CREAR UN PRODUCER POR CADA CATEGORIA: calidad del aire, la temperatura, la humedad y los niveles de ruido (4 producers, 4 carpetas)
Tambien hay que crear un consumer para cada una de esas categorias.
medir los tiempos comparando los timestamp.

Para la parte de redis hay que enviar la consulta enviada por kafka a redis para que la almacene. Una vez ahi, se envía a rabbitmq para comparar los tiempos entre kafka y redis. comparando cual se demora mas, con diferentes tamaños 