"""
Calcula operaciones básicas entre dos números enteros.

Solicita al usuario dos números y un operador aritmético, valida las
entradas y muestra el resultado de la operación. Soporta suma, resta,
multiplicación y división.
"""


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


def continue_or_exit():
    my_list = [
        'Ingrese una opción', 
        '1. Continuar', 
        '2. Salir: ', 
    ]
    while True:
        try:
            choice = int(input('\n' + '\n'.join(my_list)).strip())
            if choice == 1:
                return True
            elif choice == 2:
                print('Hasta pronto')
                return False
            else:
                print('Opción no valida')
          
        except ValueError:
            print('Ingrese un número entero')


print("CALCULADORA BÁSICA")

while True:
    first_number = validate_number("\ningrese un número: ")
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
    
    if not continue_or_exit():
        break
