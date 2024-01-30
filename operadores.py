x = 22

print("x      =        {: >6b}".format(x))        # Representación binaria de x
print("x & 4  = {: >3d} = {: >6b}".format(x & 4, x & 4))  # AND bit a bit con 4
print("x | 1  = {: >3d} = {: >6b}".format(x | 1, x | 1))  # OR bit a bit con 1
print("x ^ 4  = {: >3d} = {: >6b}".format(x ^ 4, x ^ 4))  # XOR bit a bit con 4
print("~x     = {: >3d} = {: >6b}".format(~x, ~x))        # Complemento a uno de x
print("x << 1 = {: >3d} = {: >6b}".format(x << 1, x << 1))  # Desplazamiento a la izquierda por 1
print("x >> 2 = {: >3d} = {: >6b}".format(x >> 2, x >> 2))  # Desplazamiento a la derecha por 2