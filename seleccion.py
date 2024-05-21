def selection_sort(arr):
    # Recorremos todo el array
    for i in range(len(arr)):
        # Encuentra el mínimo elemento en el resto del array sin ordenar
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # Intercambiamos el mínimo elemento encontrado con el primer elemento
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# Ejemplo de uso
mi_lista = [64, 34, 25, 12, 22, 11, 90]
selection_sort(mi_lista)
print("Lista ordenada:", mi_lista)
