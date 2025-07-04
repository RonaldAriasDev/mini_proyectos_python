# Crea un programa que pida un número al usuario y devuelva si es par o impar

print("PAR O IMPAR")

numero = input("Ingrese un número: ").strip()

try:
  numero_int = int(numero)
  if (numero_int % 2) == 0:
    print(f"El número {numero_int} es par")
  else:
    print(f"El número {numero_int} es impar")
except ValueError:
  print("por favor ingrese un número entero, no decimal, ni en texto")

