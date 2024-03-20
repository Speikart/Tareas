def generate_spiral(square_size):
    # Función para generar el cuadrado en espiral
    # Crea una matriz de tamaño square_size x square_size inicialmente llena de ceros
    spiral = [[0 for _ in range(square_size)] for _ in range(square_size)]
    num = 1
    generate_recursive(spiral, 0, 0, square_size, num) # Llama a la función recursiva para generar los números en espiral
    return spiral

def generate_recursive(spiral, x, y, size, num):
    # Función recursiva para generar los números en espiral y asignarlos a la matriz
    if size <= 0:
        return

    # (lado superior)
    for i in range(size):
        spiral[y][x + i] = num
        num += 1

    #  (lado derecho)
    for i in range(1, size):
        spiral[y + i][x + size - 1] = num
        num += 1

    #  (lado inferior)
    for i in range(size - 2, -1, -1):
        spiral[y + size - 1][x + i] = num
        num += 1

    #  (lado izquierdo)
    for i in range(size - 2, 0, -1):
        spiral[y + i][x] = num
        num += 1

    # Llamada recursiva para generar el siguiente cuadrado interior
    generate_recursive(spiral, x + 1, y + 1, size - 2, num)

def print_spiral(spiral):
    # Función para imprimir la matriz en forma de cuadrado
    for row in spiral:
        print(" ".join(str(cell) for cell in row))

def main():
    # Función principal
    while True:
        try:
            size = int(input("Ingrese el tamaño del cuadrado (1x1, 2x2, 3x3, etc.): "))
            if size < 1:
                print("Ingrese un tamaño válido.")
                continue
            break
        except ValueError:
            print("Por favor, ingrese un número válido.")

    spiral = generate_spiral(size) # Genera el cuadrado en espiral
    print("\nEl cuadrado en espiral de tamaño {}x{} es:\n".format(size, size))
    print_spiral(spiral) # Imprime el cuadrado en espiral

if __name__ == "__main__":
    main() # Llama a la función principal si se ejecuta este script como programa principal
