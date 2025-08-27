# 📌 Cálculo de un elemento de la sucesión de Fibonacci
# Este mini proyecto consiste en un programa que:
# Solicita al usuario que ingrese una posición en la sucesión de Fibonacci.
# Valida que la entrada sea un número entero no negativo.
# Calcula el valor correspondiente a esa posición utilizando una función recursiva.
# Muestra el resultado al usuario.
# La sucesión de Fibonacci comienza así: 0, 1, 1, 2, 3, 5, 8, 13, 21...


def validate_prompt():
  while True:
    try:
      position = int(input('Ingrese una posición: ').strip())
      if position >= 0:
        return position
      else:
        print('La posición no puede ser negativa')
    except ValueError:
      print('Ingrese un número entero')


def fibonacci(n):
  if n == 0:
    return 0
  elif n == 1:
    return 1
  else:
    return fibonacci(n-1) + fibonacci(n-2)


print('CÁLCULO DE UN ELEMENTO DE LA SUCESIÓN DE FIBONACCI')

while True:
  position = validate_prompt()
  fibonacci_value = fibonacci(position)
  print(f'El valor que corresponde a la posición {position} es {fibonacci_value}')

"""
Ejemplo de arbol recursivo si se pasa la posición 4 a la función.
Por falta de espacio no se pondra el return en las ramas.

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
