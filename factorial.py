# 📌 Cálculo del factorial de un número
# El programa pide al usuario que ingrese un número entre 1 y 100.
# Verifica que la entrada sea válida y esté dentro del rango permitido.
# Devuelve el factorial de ese número usando una función recursiva.


def validate_prompt():
  while True:
    try:
      number = int(input('Ingrese un número entre 0 y 100: ').strip())
      if 0 <= number <= 100:
        return number
      else:
        print('El número que ingreso esta fuera de rango')
    except ValueError:
      print('Ingrese un número entero')


def factorial(n: int):
  if n == 0:
    return 1
  else: 
    return n * factorial(n-1)


print('CÁLCULO DEL FACTORIAL')
  
while True:
  number = validate_prompt() 
  number_factorial = factorial(number)
  print(f'El factorial de {number} es {number_factorial}')

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
