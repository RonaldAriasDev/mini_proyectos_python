# 📌 Simulación de una Impresora Compartida
# Este programa implementa una simulación del mecanismo de impresión utilizando la estructura de datos cola (FIFO).  
# Funcionalidades:
# Permite enviar documentos a la cola de impresión (como si fueran enviados desde distintos dispositivos).  
# Muestra en todo momento los documentos en cola.  
# Opción para imprimir el primer documento en la cola.  
# Opción para imprimir todos los documentos en orden.  
# Muestra qué documento se está imprimiendo.  
# Actualiza y muestra la cola restante después de cada impresión.


def validate_menu():
  my_list = [
    'Ingrese una opción', 
    '1. Enviar documento a la impresora', 
    '2. Ir a la impresora', 
    '3. Salir del programa: '
    ]
  while True:
    try:
      menu_option = int(input('\n'.join(my_list)).strip())
      if menu_option in [1, 2, 3]:
        return menu_option
      else:
        print('Opción no válida')
    except ValueError:
      print('Ingrese un número entero')


def add_documents():
  while True:
    document = input(
      'Añade un documento o ingrese "exit" para terminar: ').strip().title()
    if document != "Exit":
      queue.append(document)
      print('Documento enviado a la impresora')
    else:
      break
  

def validate_printer_option():
  my_list = [
    'Ingrese una opción', 
    '1. Imprimir documento en cola', 
    '2. Imprimir todos', 
    '3. Regresar: '
    ]
  while True:
    try:
      printer_option = int(input('\n'.join(my_list)).strip())
      if printer_option in [1, 2, 3]:
        return printer_option
      else:
        print('Opción no válida')
    except ValueError:
      print('Ingrese un número entero')


def printer():
  while True:
    print(f'Documentos en cola: {queue}')
    printer_option = validate_printer_option()

    match printer_option:
      case 1:
        if len(queue) >= 1:
          print(f'Imprimiendo {queue[0]}')
          queue.pop(0)
        else:
          print('No hay documentos en cola')
      case 2:
        if len(queue) >= 1:
          print(f'Imprimiendo {queue}')
          queue.clear()
        else:
          print('No hay documentos en cola')
      case 3:
        print('Volviendo al menu principal')
        break


queue = []

while True:
  menu_option = validate_menu()

  match menu_option:
    case 1:
      add_documents()
    case 2:
      printer()
    case 3:
      print('Hasta pronto')
      break
