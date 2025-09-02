"""
Calcula el factorial de un número

- Pide al usuario que ingrese un número entre 0 y 100.
- Verifica que la entrada sea válida y esté dentro del rango permitido.
- Devuelve el factorial de ese número usando una función recursiva.
"""

def validate_prompt():
    while True:
        try:
            number = int(input('\nIngrese un número entre 0 y 100: ').strip())
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


print('CÁLCULO DEL FACTORIAL')
  
while True:
    number = validate_prompt() 
    number_factorial = factorial(number)
    print(f'El factorial de {number} es {number_factorial}')
    if not continue_or_exit():
        break

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

Se llega al caso base, la función toma el valor y se comienza a resolver cada 
función desde la hoja hasta la raíz
"""
