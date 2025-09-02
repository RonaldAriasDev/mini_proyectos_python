"""
Simula la navegación atrás y adelante en un navegador web.

Valida entradas numéricas dentro del rango de opciones y utiliza pilas para:
- Ingresar a una página.
- Ir atrás.
- Ir adelante.
"""


def validate_prompt():
    options = [
        '\nIngrese una opción', 
        '1. Buscar', 
        '2. Atrás', 
        '3. Adelante', 
        '4. Salir: '
    ]
    while True:
        try:
            option = int(input('\n'.join(options)).strip())
            if 1 <= option <= 4:
                return option
            else:
                print('Opción no válida')
        except ValueError:
            print('Ingrese un número entero')


def enter_url():
    web_page = input('Ingresar dirección web: ').strip()
    return web_page
  
 
print('NAVEGADOR WEB')
my_list1 = []  
my_list2 = []

while True:
    option = validate_prompt()
    
    match option:
        case 1:
            web_page = enter_url()
            my_list1.append(web_page)
            my_list2.clear()
            print(f'Estás en la página de {my_list1[-1]}')
        case 2:
            if len(my_list1) >= 2:
                my_list2.append(my_list1.pop())
                print(f'Estás en la página de {my_list1[-1]}')
            else:
                print('No es posible ir atrás')
        case 3:
            if len(my_list2) >= 1:
                my_list1.append(my_list2.pop())
                print(f'Estás en la página de {my_list1[-1]}')
            else:
                print('No es posible ir adelante')
        case 4:
            print('Hasta pronto')
            break
