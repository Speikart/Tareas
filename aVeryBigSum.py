import os

def aVeryBigSum(ar):
    # Inicializar la suma como cero
    total_sum = 0
    
    # Sumar todos los elementos en la lista
    for num in ar:
        total_sum += num
    
    # Devolver la suma total
    return total_sum

if __name__ == '__main__':
    # Leer la cantidad de elementos en la lista
    ar_count = int(input().strip())

    # Leer los elementos de la lista
    ar = list(map(int, input().rstrip().split()))

    # Calcular la suma de los elementos de la lista
    result = aVeryBigSum(ar)

    # Escribir el resultado en un archivo de salida
    with open('output.txt', 'w') as fptr:
        fptr.write(str(result) + '\n')
