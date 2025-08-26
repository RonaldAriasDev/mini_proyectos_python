# Calculadora básica que permite realizar operaciones de suma, resta, multiplicación y división entre dos números enteros. 
# El programa solicita al usuario los dos números y el operador a utilizar, incluye validación de entradas y muestra el resultado de la operación.


def validate_number(prompt: str):
  while True:
    try:
      validated_number = int(input(prompt).strip())
      return validated_number
    except ValueError:
      print('Ingrese un número entero')


def validate_operator(prompt: str):
  while True:
    operator = input(prompt).strip()
    operators = ['+', '-', '*', '/']
    if operator in operators:
      return operator
    else:
      print('Ingrese un operador válido')


print("CALCULADORA BÁSICA")

while True:
  print(' ')
  first_number = validate_number("ingrese un número: ")
  operator = validate_operator("ingrese un operador (+, -, *, /): ")
  second_number = validate_number("ingrese un número: ")
  
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
