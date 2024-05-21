def metodo_burbuja(arr):
    # Recorremos todo el array
    for i in range(len(arr)):
        # Últimos i elementos ya están ordenados
        for j in range(0, len(arr) - i - 1):
            # Intercambiamos si el elemento encontrado es mayor que el siguiente
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Ejemplo de uso
mi_lista = [64, 34, 25, 12, 22, 11, 90]
metodo_burbuja(mi_lista)
print("Lista ordenada:", mi_lista)
