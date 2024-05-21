def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)

# Ejemplo de uso
mi_lista = [64, 34, 25, 12, 22, 11, 90]
mi_lista = quick_sort(mi_lista)
print("Lista ordenada:", mi_lista)
