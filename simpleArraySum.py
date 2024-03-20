import os

# Definir la ruta del archivo de salida
output_path = "./output.txt"

def simpleArraySum(ar):
    # Sumar todos los elementos en el array
    return sum(ar)

if __name__ == '__main__':
    # Abrir el archivo de salida en modo escritura
    with open(output_path, 'w') as fptr:
        # Leer la cantidad de elementos en la lista
        ar_count = int(input().strip())

        # Leer los elementos de la lista
        ar = list(map(int, input().rstrip().split()))

        # Calcular la suma de los elementos de la lista
        result = simpleArraySum(ar)

        # Escribir el resultado en el archivo de salida
        fptr.write(str(result) + '\n')
