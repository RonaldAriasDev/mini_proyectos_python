# 📌 Cálculo del factorial de un número
# El programa pide al usuario que ingrese un número.
# Devuelve el factorial de ese número usando una función.

def factorial(n: int):
  if n == 0:
    return 1
  else: 
    return n * factorial(n-1)

print('CÁLCULO DEL FACTORIAL')
number = int(input(' \nIngrese un número: '))
number_factorial = factorial(number)
print(f' \nEl factorial de {number} es {number_factorial}')

"""
Ejemplo de árbol recursivo cuando se pasa el valor 5 a la función.

factorial(5)
|
|__return 5 * factorial(4)
              |
              |__return 4 * factorial(3)
                            |
                            |__return 3 * factorial(2)
                                          |
                                          |__return 2 * factorial(1)
                                                        |
                                                        |__return 1 * factorial(0)
                                                                      |
                                                                      |__return 1
# se llega al caso base, la función toma el valor y se comienza a resolver cada función desde la hoja hasta la raíz
"""
