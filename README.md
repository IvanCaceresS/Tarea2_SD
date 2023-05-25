# Sistemas_Dristribuidos_T2

# -------------FUNCIONAMIENTO KAFKA--------------

cd .\Prueba_kafka\
docker compose up --build

INICIAR PRODUCERS Y CONSUMERS

docker exec -it producer_elefante_kafka bash
docker exec -it producer_girafa_kafka bash
docker exec -it producer_leon_kafka bash
docker exec -it producer_mono_kafka bash
docker exec -it producer_tigre_kafka bash

docker exec -it consumer_elefante_kafka bash
docker exec -it consumer_girafa_kafka bash
docker exec -it consumer_leon_kafka bash
docker exec -it consumer_mono_kafka bash
docker exec -it consumer_tigre_kafka bash

# -------------FUNCIONAMIENTO RABBITMQ-----------

cd .\Prueba_Rabbit\
docker compose up --build

INICIAR PRODUCERS Y CONSUMERS

docker exec -it producer_elefante_rabbit bash
docker exec -it producer_girafa_rabbit bash
docker exec -it producer_leon_rabbit bash
docker exec -it producer_mono_rabbit bash
docker exec -it producer_tigre_rabbit bash

docker exec -it consumer_elefante_rabbit bash
docker exec -it consumer_girafa_rabbit bash
docker exec -it consumer_leon_rabbit bash
docker exec -it consumer_mono_rabbit bash
docker exec -it consumer_tigre_rabbit bash

# -------------FUNCIONAMIENTO CON REDIS----------

d .\Prueba_redis\
docker compose up --build

docker exec -it producer_elefante_kafka bash
docker exec -it consumer_elefante_kafka bash
docker exec -it producer_elefante_rabbit bash
docker exec -it consumer_elefante_rabbit bash

# Botar sistema
docker compose down -v