import matplotlib.pyplot as plt

# Leer los datos del primer archivo de texto
with open('./kafka_latencia_5seg_200k.txt', 'r') as file:
    data1 = file.read().splitlines()
    data1 = [float(value) for value in data1]

# Leer los datos del segundo archivo de texto
with open('./rabbit_latencia_5seg_200k.txt', 'r') as file:
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
ax.set_ylabel('Tiempo (segundos)')

# Configurar título del gráfico
ax.set_title('Gráfico de Datos')

# Agregar leyenda
ax.legend()

# Mostrar el gráfico
plt.show()
