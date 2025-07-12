"""
Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no numéricos y con más de 11 dígitos (o el número de dígitos que quieras)
 * - También se debe proponer una operación de finalización del programa.
"""


def menu():
  opcion = input("Seleccione una opción de acuerdo a la función que desea realizar. 1) Mostrar todos. 2) Buscar. 3) Agregar. 4) Actualizar. 5) Eliminar. 6) Salir.: ")
  return opcion
  

def mostrar_todos():
  print(agenda)

  
def buscar():
  buscar_nombre = input("Ingrese un nombre: ")
  if buscar_nombre.lower().strip() in agenda:
    print(agenda[buscar_nombre.lower().strip()])
  else:
    print("Contacto no encontrado")
    
    
def agregar():
  agregar_numero = input("Ingrese un número de nueve digitos como máximo: ")
  if len(agregar_numero.strip()) <= 9:
    agregar_nombre = input("Ingrese un nombre: ")
    agenda[agregar_nombre.lower().strip()] = agregar_numero.strip()
    print("Contacto guardado correctamente")
  else:
    print("La cantidad de digitos es superior a la establecida")
    
    
def actualizar():
  actualizar_contacto = input("Ingrese un nombre: ")
  actualizar_numero = input("Ingrese el número actualizado. Debe tener máximo nueve digitos: ")
  if len(actualizar_numero.strip()) <= 9:
    agenda[actualizar_contacto.lower().strip()] = actualizar_numero.strip()
    print("Contacto actualizado correctamente")
  else:
    print("La cantidad de digitos es superior a la establecida")
    
    
def eliminar():
  eliminar_contacto = input("ingrese un nombre: ")
  if eliminar_contacto.lower().strip() in agenda:
    del agenda[eliminar_contacto.lower().strip()]
    print("Contacto eliminado correctamente")
  else:
    print("Contacto no encontrado")


def salir():
  print("Hasta pronto")


def opcion_invalida():
  print("Ingrese una opción valida")
  
  
def dato_invalido():
  print("Ingrese la opción con un número entero")

  
agenda = {"emergencia": "133"}
print("AGENDA TELEFÓNICA")

x = 1
while x == 1:
  opcion = menu()
  try:
    opcion_int = int(opcion)
    if opcion_int == 1:
      mostrar_todos()
    elif opcion_int == 2:
      buscar()
    elif opcion_int == 3:
      agregar()
    elif opcion_int == 4:
      actualizar()
    elif opcion_int == 5:
      eliminar()
    elif opcion_int == 6:
      x = 2
      salir()
    else:
      opcion_invalida()  
  except ValueError:
    dato_invalido()