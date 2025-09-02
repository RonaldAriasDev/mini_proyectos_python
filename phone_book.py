"""
Gestiona una agenda de contactos por terminal.

Permite realizar distintas operaciones sobre la lista de contactos:
- Mostrar todos los contactos.
- Buscar un contacto por nombre.
- Añadir un nuevo contacto (número máximo: 9 dígitos).
- Actualizar el número de un contacto existente.
- Eliminar un contacto.
- Finalizar el programa.
"""


def validate_menu_option():
    my_list = [
        'Seleccione una opción:', 
        '1. Mostrar contactos', 
        '2. Buscar por nombre', 
        '3. Agregar', 
        '4. Actualizar', 
        '5. Eliminar', 
        '6. Salir: '
    ]
    
    while True:
        try:
            menu_option = int(input('\n' + '\n'.join(my_list)).strip())
            if 1 <= menu_option <= 6:
                return menu_option
            else:
                print('Ingrese una opción válida')
        except ValueError:
            print('Ingrese un número entero')
  

def show_contacts():
    if len(contacts) >= 1:
        print(contacts)
    else:
        print('No hay contactos registrados')
  

def validate_name():
    while True:
        validated_name = input('Ingrese un nombre: ').strip()
        if all(word.isalpha() for word in validated_name.split()):
            return validated_name.title()
        else:
            print('Ingrese solo letras')

  
def search_contact(name):
    if name in contacts:
        print(f'El número de {name} es {contacts[name]}')
    else:
        print('Contacto no encontrado')
  

def validate_number():
    while True:
        try:
            validated_number = int(
                input('Ingrese un número de nueve digitos como máximo: ').strip()
            )
            if 1 <= len(str(validated_number)) <= 9:
                return validated_number
            else:
                print('Ingrese entre 1 y 9 dígitos')
        except ValueError:
            print('Ingrese un número entero')
 
 
def add_contact(name, number):
    contacts[name] = number
    print('Contacto guardado correctamente')


def update_contact(name, number):
    contacts[name] = number
    print('Contacto actualizado correctamente')
  

def delete_contact(name):
    if name in contacts:
        del contacts[name]
        print('Contacto eliminado correctamente')
    else:
        print('Contacto no encontrado')


def exit():
    print('Hasta pronto')


print("AGENDA TELEFÓNICA")
contacts = {}

while True:
    menu_option = validate_menu_option()
    
    if menu_option == 1:
        show_contacts()
    elif menu_option == 2:
        name = validate_name()
        search_contact(name)
    elif menu_option == 3:
        name = validate_name()
        number = validate_number()
        add_contact(name, number)
    elif menu_option == 4:
        name = validate_name()
        number = validate_number()
        update_contact(name, number)
    elif menu_option == 5:
        name = validate_name()
        delete_contact(name)
    elif menu_option == 6:
        exit()
        break
