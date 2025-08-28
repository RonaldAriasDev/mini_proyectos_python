# 📌 Simulación del mecanismo de navegación (atrás/adelante) de un navegador web
# Valida que la entrada del usuario sea un número entero y esté dentro del rango de las opciones disponibles.
# Utiliza pilas para implementar las siguientes acciones:
# Ingresar a una página.
# Ir atrás.
# Ir adelante. 


def validate_prompt():
  options = [
    '1. Buscar', 
    '2. Atrás', 
    '3. Adelante: '
    ]
  while True:
    try:
      option = int(input(' \n' 'Ingrese una opción\n' + '\n'.join(options)).strip())
      if 1 <= option <= 3:
        return option
      else:
        print('Opción no válida')
    except ValueError:
      print('Ingrese un número entero')


def enter_url():
  web_page = input('Ingresar dirección web: ').strip()
  return web_page
 
 
print('Firefox')
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
        print(f'Estás en la página de  {my_list1[-1]}')
      else:
        print('No es posible ir atrás')
    case 3:
      if len(my_list2) >= 1:
        my_list1.append(my_list2.pop())
        print(f'Estás en la página de {my_list1[-1]}')
      else:
        print('No es posible ir adelante')
    case _:
      pass
