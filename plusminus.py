import math
import os
import random
import re
import sys

def plusMinus(arr):
    # Inicializar contadores
    positive_count = 0
    negative_count = 0
    zero_count = 0
    
    # Contar los números positivos, negativos y cero en la lista
    for num in arr:
        if num > 0:
            positive_count += 1
        elif num < 0:
            negative_count += 1
        else:
            zero_count += 1
    
    # Calcular las proporciones
    n = len(arr)
    positive_ratio = positive_count / n
    negative_ratio = negative_count / n
    zero_ratio = zero_count / n
    
    # Imprimir las proporciones
    print(positive_ratio)
    print(negative_ratio)
    print(zero_ratio)

if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    plusMinus(arr)
