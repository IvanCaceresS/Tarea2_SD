import matplotlib.pyplot as plt

x = []  # Lista para almacenar los valores del primer gráfico
y = []  # Lista para almacenar los valores del segundo gráfico

# Leer el archivo de texto y extraer los datos
with open('latencias_redis_0seg_data_pesada.txt', 'r') as file:
    for line in file:
        data = line.strip().split('|')
        x.append(float(data[0]))
        y_value = float(data[1]) if data[1] != "None" else 0.0
        y.append(y_value)

# Graficar los datos
plt.plot(x, 'b-', label='Latencia de RabbitMQ')
plt.plot(y, 'r-', label='Latencia de Kafka')

# Personalizar el gráfico
plt.xlabel('N° de mensaje')
plt.ylabel('Latencia (segundos)')
plt.title('Latencias medidas con ayuda de Redis, mensajes livianos cada 0 segundos')
plt.legend()

# Mostrar el gráfico
plt.show()
