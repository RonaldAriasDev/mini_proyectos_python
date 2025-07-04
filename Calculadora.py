# Calculadora Básica con operadores +, -, *, / incluye validación de entrada y manejo de excepciones.

print("CALCULADORA BÁSICA. Use operadores +, -, *, /")
numero = input("ingrese un número: ")
operador = input("ingrese un operador: ")
numero1 = input("ingrese un número: ")

try:
  numero_int = int(numero)
  numero1_int = int(numero1)
  if operador == "+":
    print(numero_int + numero1_int)
  elif operador == "-":
    print(numero_int - numero1_int)
  elif operador == "*":
    print(numero_int * numero1_int)
  elif operador == "/":
    try:
      print(numero_int / numero1_int)
    except ZeroDivisionError:
      print("No es posible dividir entre 0")
  else:
    print("operador invalido")
except ValueError:
  print("Los valores ingresados deben ser números enteros")


