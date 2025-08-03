"""
Calcular el factorial de un número concreto (la función recibe ese número).
"""

def factorial(n: int):
  if n == 0:
    return 1
  else: 
    return n * factorial(n-1)

print(factorial(5))

"""
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


"""
Calcular el valor de un elemento concreto (según su posición) en la sucesión de Fibonacci (la función recibe la posición).
0, 1, 1, 2, 3, 5, 8, 13, 21...
"""

def fibonacci(n):
  if n == 0:
    return 0
  elif n == 1:
    return 1
  else:
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(4))

"""
Por un tema de espacio no se pondra el return en las ramas

fibonacci(4)
|
|__fibonacci(3)                            +  fibonacci(2)
          |                                   |
          |__fibonacci(2) + fibonacci(1)      |__fibonacci(1) + fibonacci(0)
             |              |__1                    |__1        |__0
             |__fibonacci(1) + fibonacci(0)
                |__1           |__0

# se llega al caso base, las funciones toman su respectivo valor y se comienza a resolver cada función desde la hoja hasta la raíz
"""