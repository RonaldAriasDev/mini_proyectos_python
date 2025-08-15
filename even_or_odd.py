# 📌 Determinar si un número es par o impar
# El programa pide un número al usuario.
# Devuelve si el número es par o impar.

print("PAR O IMPAR")
number = input("Ingrese un número: ").strip()

try:
  number_int = int(number)
  if (number_int % 2) == 0:
    print(f"El número {number_int} es par")
  else:
    print(f"El número {number_int} es impar")
except ValueError:
  print("por favor ingrese un número entero, no decimal, ni en texto")
