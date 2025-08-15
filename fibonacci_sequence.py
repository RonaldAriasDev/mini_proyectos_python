# 📌 Cálculo de un elemento de la sucesión de Fibonacci
# El programa pide al usuario que ingrese una posición.
# Devuelve el valor de la sucesión de Fibonacci en esa posición usando una función.
# 0, 1, 1, 2, 3, 5, 8, 13, 21...


def fibonacci(n):
  if n == 0:
    return 0
  elif n == 1:
    return 1
  else:
    return fibonacci(n-1) + fibonacci(n-2)

print('CÁLCULO DE UN ELEMENTO DE LA SUCESIÓN DE FIBONACCI')
position = int(input('Ingrese una posición: '))
fibonacci_value = fibonacci(position)
print(fibonacci_value)

"""
Ejemplo de arbol recursivo si se pasa la posición 4
Por un tema de espacio no se pondra el return en las ramas

fibonacci(4)
|
|__fibonacci(3)                            +  fibonacci(2)
          |                                   |
          |__fibonacci(2) + fibonacci(1)      |__fibonacci(1) + fibonacci(0)
             |              |__1                    |__1        |__0
             |__fibonacci(1) + fibonacci(0)
                |__1           |__0

Se llega al caso base, las funciones toman su respectivo valor y se comienza a resolver cada función desde la hoja hasta la raíz
"""