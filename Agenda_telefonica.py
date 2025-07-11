"""
Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no numéricos y con más de 11 dígitos (o el número de dígitos que quieras)
 * - También se debe proponer una operación de finalización del programa.
"""

agenda = {"emergencia": "133"}
print("AGENDA TELEFÓNICA")
inicio = input("Bienvenido. Para continuar ingrese 1. ")

try:
  inicio_int = int(inicio)
  
  if inicio_int == 1:
    while inicio_int == 1:
      inicio = input("Para realizar una función ingrese 1. Para salir, 2: ")
      
      try:
        inicio_int = int(inicio)
        if inicio_int == 1:
          opcion = input("Seleccione una opción de acuerdo a la función que desea realizar. 1) Buscar. 2) Agregar. 3) Actualizar. 4) Eliminar: ")
          
          try:
            opcion_int = int(opcion)
            if opcion_int == 1:
              buscar_nombre = input("Ingrese un nombre: ")
              if buscar_nombre.lower().strip() in agenda:
                print(agenda[buscar_nombre.lower().strip()])
              else:
                print("Contacto no encontrado")
                
            elif opcion_int == 2:
              agregar_numero = input("Ingrese un número de nueve digitos como máximo: ")
              if len(agregar_numero.strip()) <= 9:
                agregar_nombre = input("Ingrese un nombre: ")
                agenda[agregar_nombre.lower().strip()] = agregar_numero.strip()
                print("Contacto guardado correctamente")
              else:
                print("La cantidad de digitos es superior a la establecida")
                
            elif opcion_int == 3:
              actualizar_contacto = input("Ingrese un nombre: ")
              actualizar_numero = input("Ingrese el número actualizado. Debe tener máximo nueve digitos: ")
              if len(actualizar_numero.strip()) <= 9:
                agenda[actualizar_contacto.lower().strip()] = actualizar_numero.strip()
                print("Contacto actualizado correctamente")
              else:
                print("La cantidad de digitos es superior a la establecida")
                
            elif opcion_int == 4:
              eliminar_contacto = input("ingrese un nombre: ")
              if eliminar_contacto.lower().strip() in agenda:
                del(agenda[eliminar_contacto.lower().strip()])
                print("Contacto eliminado correctamente")
              else:
                print("Contacto no encontrado")
                
            else:
              print("Ingrese una opción valida")
              
          except ValueError:
            print("Opción invalida. Por favor, ingrese la opción con un número entero")
        
        elif inicio_int == 2:
          print("Gracias por usar AGENDA TELEFÓNICA.")
        else:
          print("Ingrese una opción valida")
          inicio_int = 1
          
      except ValueError:
        print("Opción invalida. Por favor, ingrese la opción con un número entero")
        
  else:
    print("Opción invalida. Por favor, reinicie el programa e ingrese una opción valida")
    
except ValueError:
  print("Opción invalida. Por favor, reinicie el programa e ingrese un numero entero")
