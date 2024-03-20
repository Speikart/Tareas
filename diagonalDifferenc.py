import os

def diagonalDifference(arr):
    # Inicializar la suma de las diagonales
    primary_diagonal_sum = 0
    secondary_diagonal_sum = 0
    
    # Calcular la suma de la diagonal principal y la diagonal secundaria
    n = len(arr)
    for i in range(n):
        primary_diagonal_sum += arr[i][i]
        secondary_diagonal_sum += arr[i][n - i - 1]
    
    # Calcular la diferencia absoluta entre las sumas de las diagonales
    difference = abs(primary_diagonal_sum - secondary_diagonal_sum)
    
    return difference

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
