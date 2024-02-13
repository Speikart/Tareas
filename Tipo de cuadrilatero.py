def identificar_cuadrilatero(lados):
    lados_ordenados = sorted(lados)  # Ordenar los lados de menor a mayor
    if len(set(lados)) == 1:  # Si todos los lados son iguales, es un cuadrado
        return "Cuadrado"
    elif len(set(lados)) == 2:  # Si solo hay dos medidas únicas, es un rectángulo
        return "Rectángulo"
    
    else:  # Si no cumple ninguna de las anteriores, es un cuadrilátero genérico
        return "Otro cuadrilátero"

# Solicitar al usuario que ingrese las medidas de los 4 lados
lados = []
for i in range(4):
    lado = float(input("Ingresa la medida del lado {}: ".format(i+1)))
    lados.append(lado)

# Llamar a la función para identificar el tipo de cuadrilátero e imprimir el resultado
tipo_cuadrilatero = identificar_cuadrilatero(lados)
print("El cuadrilátero ingresado es un:", tipo_cuadrilatero)