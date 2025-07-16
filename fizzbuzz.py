"""
En el rango de 1 a 100, para cada elemento imprime:
fizz, si el número es divisible entre 3
buzz, si el número es dividible entre 5
fizzbuzz, si eo número es divisible entre 3 y entre 5 a la vez
"""

def fizzbuzz():
  for i in range(1,101):
    if (i % 3) == 0 and (i % 5) == 0:
      print("fizzbuzz")
    elif (i % 3) == 0:
      print("fizz")
    elif (i % 5) == 0:
      print("buzz")
    else:
      print(i)

fizzbuzz()


