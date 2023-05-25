import matplotlib.pyplot as plt

# Leer los datos del primer archivo de texto
with open('./latencia/kafka_latencia_5seg_200k.txt', 'r') as file:
    data1 = file.read().splitlines()
    data1 = [float(value) for value in data1]

# Leer los datos del segundo archivo de texto
with open('./latencia/rabbit_latencia_5seg_200k.txt', 'r') as file:
     data2 = file.read().splitlines()
     data2 = [float(value) for value in data2]

# Crear una lista de índices para el eje x
x1 = list(range(1, len(data1) + 1))
x2 = list(range(1, len(data2) + 1))

# Crear la figura y los ejes del gráfico
fig, ax = plt.subplots()

# Graficar los datos del primer archivo (rojo)
ax.plot(x1, data1, color='red', label='Kafka data pesada, 5 segundos')

# Graficar los datos del segundo archivo (azul)
ax.plot(x2, data2, color='blue', label='RabbitMq data pesada, 5 segundos')

# Configurar etiquetas del eje x y y
ax.set_xlabel('N° mensaje')
ax.set_ylabel('Latencia (segundos)')

# Configurar título del gráfico
ax.set_title('Kafka vs RabbitMq mensajes pesados cada 5 segundos')

# Agregar leyenda
ax.legend()

# Mostrar el gráfico
plt.show()



########### 5 CATEGORIAS ##################
# import matplotlib.pyplot as plt

# # Leer los datos del archivo de texto del elefante
# with open('./latencia_elefante_5seg.txt', 'r') as file:
#     data_elefante = file.read().splitlines()
#     data_elefante = [float(value) for value in data_elefante]

# # Leer los datos del archivo de texto de la jirafa
# with open('./latencia_girafa_5seg.txt', 'r') as file:
#     data_girafa = file.read().splitlines()
#     data_girafa = [float(value) for value in data_girafa]

# # Leer los datos del archivo de texto del león
# with open('./latencia_leon_5seg.txt', 'r') as file:
#     data_leon = file.read().splitlines()
#     data_leon = [float(value) for value in data_leon]

# # Leer los datos del archivo de texto del mono
# with open('./latencia_mono_5seg.txt', 'r') as file:
#     data_mono = file.read().splitlines()
#     data_mono = [float(value) for value in data_mono]

# # Leer los datos del archivo de texto del tigre
# with open('./latencia_tigre_5seg.txt', 'r') as file:
#     data_tigre = file.read().splitlines()
#     data_tigre = [float(value) for value in data_tigre]

# # Crear una lista de índices para el eje x
# x_elefante = list(range(1, len(data_elefante) + 1))
# x_girafa = list(range(1, len(data_girafa) + 1))
# x_leon = list(range(1, len(data_leon) + 1))
# x_mono = list(range(1, len(data_mono) + 1))
# x_tigre = list(range(1, len(data_tigre) + 1))

# # Crear la figura y los ejes del gráfico
# fig, ax = plt.subplots()

# # Graficar los datos del elefante (rojo)
# ax.plot(x_elefante, data_elefante, color='red', label='Elefante')

# # Graficar los datos de la jirafa (azul)
# ax.plot(x_girafa, data_girafa, color='blue', label='Girafa')

# # Graficar los datos del león (verde)
# ax.plot(x_leon, data_leon, color='green', label='León')

# # Graficar los datos del mono (naranja)
# ax.plot(x_mono, data_mono, color='orange', label='Mono')

# # Graficar los datos del tigre (morado)
# ax.plot(x_tigre, data_tigre, color='purple', label='Tigre')

# # Configurar etiquetas del eje x y y
# ax.set_xlabel('N° mensaje')
# ax.set_ylabel('Tiempo (segundos)')

# # Configurar título del gráfico
# ax.set_title('Gráfico de Datos de Latencia')

# # Agregar leyenda
# ax.legend()

# # Mostrar el gráfico
# plt.show()
