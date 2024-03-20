import math
import os
import random
import re
import sys

def miniMaxSum(arr):
    # Ordenar la lista
    arr.sort()
    
    # Calcular la suma mínima
    min_sum = sum(arr[:-1])
    
    # Calcular la suma máxima
    max_sum = sum(arr[1:])
    
    # Imprimir las sumas mínima y máxima
    print(min_sum, max_sum)

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))
    miniMaxSum(arr)
