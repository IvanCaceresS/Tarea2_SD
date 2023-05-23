import random
import string

def generate_random_data(min_length, max_length):
    length = random.randint(min_length, max_length)
    data = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
    return data

def generate_data_file(file_path, num_lines, min_length, max_length):
    with open(file_path, 'w') as file:
        for _ in range(num_lines):
            data = generate_random_data(min_length, max_length)
            print(_)

            file.write(data + '\n')

file_path = './datos_pesados.txt'  # Ruta del archivo de texto
num_lines = 10000  # Cantidad de líneas/datos en el archivo
min_length = 199999  # Longitud mínima del dato
max_length = 200000  # Longitud máxima del dato

generate_data_file(file_path, num_lines, min_length, max_length)
