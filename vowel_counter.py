"""
Cuenta las vocales de una palabra ingresada por el usuario.

Reemplaza las vocales acentuadas y convierte la palabra a minúsculas. 
Luego recorre cada letra indicando si es vocal o consonante, y al final
muestra la cantidad total de vocales.
"""


def validate_prompt():
    while True:
        text = input('\nIngrese una palabra: ').strip()
        if text.isalpha():
            return (
                text.replace('á','a')
                    .replace('é', 'e')
                    .replace('í','i')
                    .replace('ó', 'o')
                    .replace('ú', 'u')
                    .lower()
            )
        else:
            print('Ingrese solo letras')


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


print("CONTADOR DE VOCALES")
vowels = ['a', 'e', 'i', 'o', 'u']

while True:
    validated_prompt = validate_prompt()
    vowels_count = 0
    
    for letter in validated_prompt:
        if letter in vowels:
            print(f'{letter}: es una vocal')
            vowels_count += 1
        else:
            print(f'{letter} es una consonante')

    print(f'Cantidad de vocales en {validated_prompt}: {vowels_count}')

    if not continue_or_exit():
        break
