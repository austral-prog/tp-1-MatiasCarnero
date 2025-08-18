def math():
    a = 57
    b = 7
    return a, b

a, b = math()

num1 = a
num2 = b

suma = num1 + num2
print("Suma:", suma)

diferencia = num1 - num2
print(diferencia)

producto = num1 * num2
print(producto)

promedio = (num1 + num2) / 2
print(promedio)

if num2 != 0:
    cociente_entero = num1 // num2
    print(cociente_entero)
else:
    print("Cociente entero: No definido (división por cero)")

if num2 != 0:
    resto = num1 % num2
    print(resto)
else:
    print("Resto: No definido (división por cero)")

if num2 != 0:
    division_real = num1 / num2
    print(division_real)
else:
    print("División real: No definido (división por cero)")

