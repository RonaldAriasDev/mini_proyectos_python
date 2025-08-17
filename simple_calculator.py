# Calculadora básica que permite realizar operaciones de suma, resta, multiplicación y división entre dos números enteros. 
# El programa solicita al usuario los dos números y el operador a utilizar, incluye validación de entradas y muestra el resultado de la operación.


print("CALCULADORA BÁSICA")
first_input = input("ingrese un número: ")
operator = input("ingrese un operador (+, -, *, /): ")
second_input = input("ingrese un número: ")

try:
  first_number = int(first_input)
  second_number = int(second_input)
  if operator == "+":
    print(first_number + second_number)
  elif operator == "-":
    print(first_number - second_number)
  elif operator == "*":
    print(first_number * second_number)
  elif operator == "/":
    try:
      print(first_number / second_number)
    except ZeroDivisionError:
      print("No es posible dividir entre 0")
  else:
    print("operador invalido")
except ValueError:
  print("Los valores ingresados deben ser números entero
  s")
