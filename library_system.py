"""
Gestiona un sistema de biblioteca.

Simula la administración de libros, revistas y películas, cada uno con
atributos específicos: libros con autor y número de páginas, revistas
con número de edición y mes de publicación, y películas con director
y duración.

Incluye funciones para registrar materiales, listarlos y buscarlos
por título, mostrando la información correspondiente según su tipo.
"""


class Library:
    def __init__(self, title: str, year: int):
        self.title = title
        self.year = year
    
    def __str__(self):
        return (
            f'\nTitulo: {self.title}\n'
            f'Año de publicación: {self.year}'
        )


class Book(Library):
    def __init__(
        self, 
        title: str, 
        year: int, 
        author: str, 
        number_pages: int
    ):
        super().__init__(title, year)
        self.author = author
        self.number_pages = number_pages

    def __str__(self):
        return (
            f'\nTitulo: {self.title}\n'
            f'Año de publicación: {self.year}\n'
            f'Autor: {self.author}\n'
            f'Número de páginas: {self.number_pages}'
        )


class Magazine(Library):
    def __init__(
        self, 
        title: str, 
        year: int, 
        edition_number: int, 
        publication_month: str
    ):
        super().__init__(title, year)
        self.edition_number = edition_number
        self.publication_month = publication_month

    def __str__(self):
        return (
            f'\nTitulo: {self.title}\n'
            f'Año de publicación: {self.year}\n'
            f'Número de edición: {self.edition_number}\n'
            f'Mes de publicación: {self.publication_month}'
        )


class Movie(Library):
    def __init__(
        self, 
        title: str, 
        year: int, 
        director: str, 
        duration_minutes: int
    ):
        super().__init__(title, year)
        self.director = director
        self.duration_minutes = duration_minutes

    def __str__(self):
        return (
            f'\nTitulo: {self.title}\n'
            f'Año de publicación: {self.year}\n'
            f'Director: {self.director}\n'
            f'Duración (minutos): {self.duration_minutes}'
        )


class Archive:
  
    def __init__(self):
        self.materials = []
    
    def add(self, material):
        self.materials.append(material)
    
    def show_materials(self):
        if self.materials:
            for material in self.materials:
                print(material)
        else:
            print(f'No se ha registrado ningún material.')
        
    def search_material(self):
        title = validate_word('\nIngrese el título del material: ')
        for material in self.materials:
            if material.title == title:
                print(material)
                break
        else:
            print(f'\n{title} no está registrado')

storage = Archive()


def validate_word(text: str):
    while True:
        prompt = input(text).strip()
        if all(word.isalpha() for word in prompt.split()):
            return prompt.title()
        else:
            print('Ingrese solo letras')


def validate_choice(prompt, min_val, max_val, islist=False):
    while True:
        try:
            text = '\n' + '\n'.join(prompt) if islist else prompt
            user_choice = int(input(text))

            if min_val <= user_choice <= max_val:
                return user_choice
            else:
                print(f"Ingrese un número entre {min_val} y {max_val}")
        except ValueError:
            print("Ingrese un número entero")


def add_book():
    print('\nIngrese los datos a continuación')
    title = validate_word('Titulo: ')
    year = validate_choice('Año de publicación: ', 0, 2025)
    author = validate_word('Autor: ')
    number_pages = validate_choice('Número de páginas: ', 1, 1000)
    new_book = Book(title, year, author, number_pages)
    storage.add(new_book)
    print('Libro agregado con éxito')


def add_magazine():
    print('\nIngrese los datos a continuación')
    title = validate_word('Titulo: ')
    year = validate_choice('Año de publicación: ', 1900, 2025)
    edition_number = validate_choice('Edicición n•: ', 1, 120)
    publication_month = validate_word('Més de publicación: ')
    new_magazine = Magazine(title, year, edition_number, publication_month)
    storage.add(new_magazine)
    print('Revista agregada con éxito')

  
def add_movie():
    print('\nIngrese los datos a continuación')
    title = validate_word('Titulo: ')
    year = validate_choice('Año de publicación: ', 1900, 2025)
    director = validate_word('Director: ')
    duration_minutes = validate_choice('Duración en minutos: ', 1, 300)
    new_movie = Movie(title, year, director, duration_minutes)
    storage.add(new_movie)
    print('Película agregada con éxito')


menu_options = [
    'Seleccione una opción:', 
    '1. Registrar material', 
    '2. Mostrar todos los materiales', 
    '3. Buscar material por título', 
    '4. Salir: '
]

material_types = [
    'Seleccione el tipo de material', 
    '1. Libro', 
    '2. Revista', 
    '3. Pelicúla: '  
]

print('SISTEMA DE LIBRERIA\nBienvenido')

while True:
    menu_option = validate_choice(menu_options, 1, 4, True)
    
    match menu_option:
        case 1:
            material_type = validate_choice(material_types, 1, 3, True)
            if material_type == 1:
                add_book()
            elif material_type == 2:
                add_magazine()
            elif material_type == 3:
                add_movie()
        
        case 2:
            storage.show_materials()
        
        case 3:
            storage.search_material()

        case 4:
            print('\nHasta pronto')
            break
