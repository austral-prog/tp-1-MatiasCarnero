[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/WZSesQx9)
# Trabajo Práctico 1

## Ejercicio 1

Para este ejercicio el objetivo es leer el código, anotar lo que piensen que los prints vayan a decir y luego correr el código para ver si les dio igual o no.

```python
i1 = 3
i2 = 5
i3 = i2 + i1
print("valor de i1:")
print(i1)
print("valor de i2:")
print(i2)
print("valor de i3:")
print(i3)
print(i1 + i2 + i3)

s1, s2, s3 = "Python", " is ", 'awesome'
print(s1 + s2 + s3)

x = y = z = "Naranja"
print("valor de x: " + x + ", valor de y: " + y + ", valor de z: " + z)

z1 = i3 / i2
print(z1)
z2 = i3 % i2
print(z2)
f1 = -.5
f2 = 10
f3 = f1 + f2
i3 = int(f3)
print("entero i3:")
print(i3)
print("variable f3:")
print(f3)
f2 += i1
print("el valor de")
print(f2)
print("más")
print(f1)
print("es:")
print(f2 + f1)

```
valor de i1:
3
valor de i2:
5
valor de i3:
8
16
Python is awesome
valor de x: Naranja, valor de y: Naranja, valor de z: Naranja
1.6
3
entero i3:
9
variable f3:
9.5
el valor de
13
más
-0.5
es:
12.5
## Ejercicio 2 - Math

Escribir un programa dentro de exercise_math.py que dado dos números enteros imprima en pantalla el resultado de las siguientes operaciones: la suma, la diferencia, el producto, el promedio, el cociente entero y el resto de la división entera y el valor real de la división. Para entregar correctamente se deberá imprimir dichos resultados en el orden que fueron pedidos en la consigna. Por ejemplo, primero la suma, despues la diferencia, y asi sucesivamente.

Ejemplo: Para a = 57 y b = 7 el output debera ser:

```python
64
50
399
32.0
8
1
8.142857142857142
```
num1 = int(input("Ingrese el primer número entero: "))
num2 = int(input("Ingrese el segundo número entero: "))

# 1. Suma
suma = num1 + num2
print("Suma:", suma)

# 2. Diferencia
diferencia = num1 - num2
print("Diferencia:", diferencia)

# 3. Producto
producto = num1 * num2
print("Producto:", producto)

# 4. Promedio
promedio = (num1 + num2) / 2
print("Promedio:", promedio)

# 5. Cociente entero (división entera)
if num2 != 0:
    cociente_entero = num1 // num2
    print("Cociente entero:", cociente_entero)
else:
    print("Cociente entero: No definido (división por cero)")

# 6. Resto de la división entera
if num2 != 0:
    resto = num1 % num2
    print("Resto:", resto)
else:
    print("Resto: No definido (división por cero)")

# 7. Valor real de la división
if num2 != 0:
    division_real = num1 / num2
    print("División real:", division_real)
else:
    print("División real: No definido (división por cero)")

