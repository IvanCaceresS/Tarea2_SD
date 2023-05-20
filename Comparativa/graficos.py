import matplotlib.pyplot as plt

# Leer los datos del archivo de texto
with open('./kafka_latencia_5seg.txt', 'r') as file:
    data = file.read().splitlines()
    data = [float(value) for value in data]

# Crear una lista de índices para el eje x
x = list(range(1, len(data) + 1))

# Crear la figura y los ejes del gráfico
fig, ax = plt.subplots()

# Graficar los datos
ax.plot(x, data)

# Configurar etiquetas del eje x y y
ax.set_xlabel('Índice')
ax.set_ylabel('Valor')

# Configurar título del gráfico
ax.set_title('Gráfico de Datos')

# Mostrar el gráfico
plt.show()

