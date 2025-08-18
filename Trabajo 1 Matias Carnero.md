num1 = int(input("Ingrese el primer número entero: "))
num2 = int(input("Ingrese el segundo número entero: "))
suma = num1 + num2
print("Suma:", suma)
diferencia = num1 - num2
print("Diferencia:", diferencia)
producto = num1 * num2
print("Producto:", producto)
promedio = (num1 + num2) / 2
print("Promedio:", promedio)
if num2 != 0:
    cociente_entero = num1 // num2
    print("Cociente entero:", cociente_entero)
else:
    print("Cociente entero: No definido (división por cero)")
if num2 != 0:
    resto = num1 % num2
    print("Resto:", resto)
else:
    print("Resto: No definido (división por cero)")
if num2 != 0:
    division_real = num1 / num2
    print("División real:", division_real)
else:
    print("División real: No definido (división por cero)")
