import os

def compareTriplets(a, b):
    # Inicializar puntuaciones de Alice y Bob
    score_a = 0
    score_b = 0
    
    # Comparar las listas de triplets
    for i in range(len(a)):
        if a[i] > b[i]:
            score_a += 1
        elif a[i] < b[i]:
            score_b += 1
    
    return [score_a, score_b]

if __name__ == '__main__':
    # Definir la ruta del archivo de salida
    output_path = "./output.txt"
    
    # Abrir el archivo de salida en modo escritura
    with open(output_path, 'w') as fptr:
        # Leer la lista de triplets para Alice
        a = list(map(int, input().rstrip().split()))

        # Leer la lista de triplets para Bob
        b = list(map(int, input().rstrip().split()))

        # Calcular la puntuación de Alice y Bob
        result = compareTriplets(a, b)

        # Escribir el resultado en el archivo de salida
        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')
