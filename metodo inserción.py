def insertion_sort(arr):
    # Recorremos el array desde el segundo elemento
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # Mover los elementos que son mayores que la clave, a una posición adelante
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Ejemplo de uso
mi_lista = [64, 34, 25, 12, 22, 11, 90]
insertion_sort(mi_lista)
print("Lista ordenada:", mi_lista)
