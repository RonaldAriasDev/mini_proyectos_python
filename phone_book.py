"""
Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no numéricos y con más de 11 dígitos (o el número de dígitos que quieras)
 * - También se debe proponer una operación de finalización del programa.
"""


def menu():
  option = input("Seleccione una opción de acuerdo a la función que desea realizar. 1) Mostrar todos. 2) Buscar. 3) Agregar. 4) Actualizar. 5) Eliminar. 6) Salir.: ")
  return option
  

def show_all():
  print(contacts)

  
def search():
  search_contact = input("Ingrese un nombre: ")
  if search_contact.lower().strip() in contacts:
    print(contacts[search_contact.lower().strip()])
  else:
    print("Contacto no encontrado")
    
    
def add():
  add_number = input("Ingrese un número de nueve digitos como máximo: ")
  if len(add_number.strip()) <= 9:
    if not add_number.isnumeric():
      raise ValueError("El numero ingresado debe tener solo digitos númericos")
    add_contact = input("Ingrese un nombre: ")
    contacts[add_contact.lower().strip()] = add_number.strip()
    print("Contacto guardado correctamente")
  else:
    print("La cantidad de digitos es superior a la establecida")
    
    
def update():
  update_contact = input("Ingrese un nombre: ")
  update_number = input("Ingrese el número actualizado. Debe tener máximo nueve digitos: ")
  if len(update_number.strip()) <= 9:
    contacts[update_contact.lower().strip()] = update_number.strip()
    print("Contacto actualizado correctamente")
  else:
    print("La cantidad de digitos es superior a la establecida")
    
    
def delete():
  delete_contact = input("ingrese un nombre: ")
  if delete_contact.lower().strip() in contacts:
    del contacts[delete_contact.lower().strip()]
    print("Contacto eliminado correctamente")
  else:
    print("Contacto no encontrado")


def exit():
  print("Hasta pronto")


def invalid_input():
  print("Ingrese una opción valida")
  
  
def invalid_data():
  print("Ingrese la opción con un número entero")

  
contacts = {"emergencia": "133"}
print("AGENDA TELEFÓNICA")

loop_control = 1
while loop_control == 1:
  option = menu()
  try:
    int_option = int(option)
  except ValueError:
    invalid_data()
    continue 
  if int_option == 1:
    show_all()
  elif int_option == 2:
    search()
  elif int_option == 3:
    try:
      add()
    except ValueError as e:
      print(e)
  elif int_option == 4:
    update()
  elif int_option == 5:
    delete()
  elif int_option == 6:
    loop_control = 2
    exit()
  else:
    invalid_input()  
  
