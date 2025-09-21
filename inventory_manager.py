"""
Administra inventario almacenando datos en un archivo .txt.

Cada producto se guarda con un nombre, price y quantity.
Permite añadir, consultar por nombre, actualizar, eliminar y salir.
Muestra el valor por producto y el total.
"""


class Product:
    def __init__(
        self,
        name: str,
        price: int,
        quantity: int,
    ):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.total_amount = self.price * self.quantity

    def __str__(self):
        return (
            f'\nProducto: {self.name}\n'
            f'Precio (CLP): {self.price}\n'
            f'Cantidad: {self.quantity}\n'
            f'Monto total: {self.total_amount}'
        )

    def attributes_line(self):
        return (
            f'{self.name} {self.price} {self.quantity}\n'
        )


class Storage:
    def __init__(self):
        self.products = []

    def add(self, product):
        self.products.append(product)

    def search_product(self):
        name = validate_word('\nIngrese el nombre del producto: ')
        for product in self.products:
            if product.name == name:
                print(product)
                break
        else:
            print(f'El producto "{name}" no está registrado')

    def update_product(self):
        name = validate_word('\nIngrese el nombre del producto: ')
        for product in self.products:
            
            if product.name == name:
                user_choice = [
                    'Ingrese una opción:',
                    '1. Actualizar nombre',
                    '2. Actualizar precio',
                    '3. Actualizar cantidad:\n'
                ]
                update_type = validate_number(user_choice, 1, 3, True)

                match update_type:
                    case 1:
                        new_name = validate_word(
                            'Ingrese el nombre actualizado del producto: '
                        )
                        product.name = new_name
                        print('Nombre actualizado con éxito')
                    case 2:
                        new_price = validate_number(
                            'Ingrese el precio actualizado del producto: ', 0
                        )
                        product.price = new_price
                        print(
                            'El precio se actualizó con éxito\n'
                            'Reinicie el programa para ver los cambios'
                        )
                    case 3:
                        new_quantity = validate_number(
                            'Ingrese la cantidad actualizada del producto: ', 0
                        )
                        product.quantity = new_quantity
                        print(
                            'Cantidad actualizada con éxito\n'
                            'Reinicie el programa para ver los cambios'
                        )
                break
        else:
            print(f'El producto no está registrado')

    def delete_product(self):
        name = validate_word('\nIngrese el nombre del producto: ')
        for product in self.products:
            if product.name == name:
                self.products.remove(product)
                print('El producto se ha eliminado correctamente')
                break
        else:
            print('El producto no está registrado')

storage = Storage()


def validate_word(text: str):
    while True:
        prompt = input(text).strip()
        if all(word.isalpha() for word in prompt.split()):
            return prompt.title()
        else:
            print('Ingrese solo letras')


def validate_number(prompt, min_val=None, max_val=None, islist=False):
   
    while True:
        try:
            text = '\n' + '\n'.join(prompt) if islist else prompt
            user_choice = int(input(text))

            if (min_val is None or user_choice >= min_val) and \
               (max_val is None or user_choice <= max_val):
                return user_choice

            if min_val is not None and max_val is not None:
                print(f"Ingrese un número entre {min_val} y {max_val}")
            elif min_val is not None:
                print(f"Ingrese un número mayor o igual a {min_val}")
            elif max_val is not None:
                print(f"Ingrese un número menor o igual a {max_val}")
        except ValueError:
            print("Ingrese un número entero")


def add_product():
    print('\nIngrese los datos a continuación')
    name = validate_word('Producto: ')
    price = validate_number('Precio (CLP): ', 0)
    quantity = validate_number('Cantidad: ', 0)
    new_product = Product(name, price, quantity,)
    storage.add(new_product)
    print('Producto agregado con éxito')


def read_file():
    import os

    if os.path.exists("inventory_manager.txt"):
        with open("inventory_manager.txt", "r") as file:
            for line in file:
                name, price, quantity = line.split()
                new_product = Product(name, int(price), int(quantity))
                storage.add(new_product)


def save_changes():
    if storage.products:
        with open("inventory_manager.txt", "w") as file:
            for product in storage.products:
                line = product.attributes_line()
                file.write(line)


menu_options = [
    'Seleccione una opción:', 
    '1. Añadir producto', 
    '2. Buscar producto por nombre', 
    '3. Actualizar producto', 
    '4. Eliminar producto',
    '5. Salir:\n'
]

print('ADMINISTRADOR DE INVENTARIO\nBienvenido')
read_file()

while True:
   
    menu_option = validate_number(menu_options, 1, 5, True)
    
    match menu_option:
        case 1:
            add_product()
        
        case 2:
            storage.search_product()
        
        case 3:
            storage.update_product()

        case 4:
            storage.delete_product()

        case 5:
            print('\nHasta pronto')
            save_changes()
            break

# por arreglar
# si el nombre del producto tiene mas de una palabra falla
# el nombre de prducto solo acepta letras