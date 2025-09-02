"""
Determina si un número es par o impar.

- Solicita al usuario que ingrese un número.
- Valida que la entrada sea un número válido.
- Usa el operador módulo (%) para determinar si es par o impar.
- Muestra el resultado al usuario.
"""


def validate_prompt():
    while True:
        try:
            validated_prompt = int(input('\nIngrese número: ').strip())
            return validated_prompt
        except ValueError:
            print('Ingrese un número entero')


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


print("PAR O IMPAR")

while True:
    validated_prompt = validate_prompt()
    if validated_prompt % 2 == 0:
        print(f"El número {validated_prompt} es par")
    else:
        print(f"El número {validated_prompt} es impar")

    if not continue_or_exit():
        break
