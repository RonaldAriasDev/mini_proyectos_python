'''
Este programa simula un sistema de biblioteca que administra distintos tipos de materiales: libros, revistas y películas. 
Cada material tiene un título y año de publicación, mientras que los libros incluyen el nombre del autor y número de páginas, 
las revistas incluyen el número de edición y mes de publicación, y las películas incluyen el director y duración en minutos. 
El sistema permite registrar nuevos materiales, listar todos los materiales con su información 
y buscar materiales por título. Cada tipo de material muestra su información usando un mismo método adaptado a sus datos específicos.
'''


class Library:
  def __init__(self, title: str, year: int):
    self.title = title
    self.year = year
  
  def __str__(self):
    return f' \nTitulo: {self.title}\nAño de publicación: {self.year}'


class Book(Library):
  def __init__(self, title: str, year: int, author: str, number_pages: int):
    super().__init__(title, year)
    self.author = author
    self.number_pages = number_pages

  def __str__(self):
    return f' \nTitulo: {self.title}\nAño de publicación: {self.year}\nAutor: {self.author}\nNúmero de páginas: {self.number_pages}'


class Magazine(Library):
  def __init__(self, title: str, year: int, edition_number: int, publication_month: str):
    super().__init__(title, year)
    self.edition_number = edition_number
    self.publication_month = publication_month

  def __str__(self):
    return f' \nTitulo: {self.title}\nAño de publicación: {self.year}\nNúmero de edición: {self.edition_number}\nMes de publicación: {self.publication_month}'
 
  
class Movie(Library):
  def __init__(self, title: str, year: int, director: str, duration_minutes: int):
    super().__init__(title, year)
    self.director = director
    self.duration_minutes = duration_minutes

  def __str__(self):
    return f' \nTitulo: {self.title}\nAño de publicación: {self.year}\nDirector: {self.director}\nDuración (minutos): {self.duration_minutes}'


class Archive:
  
  def __init__(self):
    self.materials = []
  
  def add(self, material):
    self.materials.append(material)
  
  def show_materials(self):
    if len(self.materials) >= 1:
      for material in self.materials:
        print(material)
    else:
      print(f'No se ha registrado ningún material.')
      
  def search_material(self):
    title = format_text(' \nIngrese el título del material: ')
    for material in self.materials:
      if material.title == title:
        print(material)
        break
    else:
      print(f' \n{title} no está registrado')

storage = Archive()


def menu():
  menu_lines = [
    'Seleccione una opción:', 
    '1. Registrar material', 
    '2. Mostrar todos los materiales', 
    '3. Buscar material por título', 
    '4. Salir'
    ]
  while True:
    try:
      menu_option = int(input(' \n' + '\n'.join(menu_lines)))
      if menu_option in [1, 2, 3, 4]:
        return menu_option
      else:
        print(' \nSeleccione una opción valida')
    except ValueError:
        print(' \nDigite un número entero')


def material_type():
  selected_option = [
    'Seleccione el tipo de material', 
    '1. Libro', 
    '2. Revista', 
    '3. Pelicúla'  
    ]
  while True:
    try:
      selected_material = int(input(' \n' + '\n'.join(selected_option)))
      if selected_material in [1, 2, 3]:
        return selected_material
      else:
        print('Seleccione una opción valida')
    except ValueError:
      print('Digite un número entero')


def format_text(text: str):
  while True:
    prompt = input(text).strip()
    if all(word.isalpha() for word in prompt.split()):
      return prompt.title()
    else:
      print('Ingrese solo letras')


def format_number(text: str, min_val: int, max_val: int):
  while True:
    try:
      formatted_number = int(input(text))
      if min_val <= formatted_number <= max_val:
        return formatted_number
      else:
        print(f'Ingrese un número entre {min_val} y {max_val}')
    except ValueError:
      print('Ingrese un número entero')


def add_book():
  print(' \nIngrese los datos a continuación')
  title = format_text('Titulo: ')
  year = format_number('Año de publicación: ', 0, 2025)
  author = format_text('Autor: ')
  number_pages = format_number('Número de páginas: ', 1, 1000)
  new_book = Book(title, year, author, number_pages)
  storage.add(new_book)
  print('Libro agregado con éxito')


def add_magazine():
  print(' \nIngrese los datos a continuación')
  title = format_text('Titulo: ')
  year = format_number('Año de publicación: ', 1900, 2025)
  edition_number = format_number('Edicición n•: ', 1, 120)
  publication_month = format_text('Més de publicación: ')
  new_magazine = Magazine(title, year, edition_number, publication_month)
  storage.add(new_magazine)
  print('Revista agregada con éxito')

  
def add_movie():
  print(' \nIngrese los datos a continuación')
  title = format_text('Titulo: ')
  year = format_number('Año de publicación: ', 1900, 2025)
  director = format_text('Director: ')
  duration_minutes = format_number('Duración en minutos: ', 1, 300)
  new_movie = Movie(title, year, director, duration_minutes)
  storage.add(new_movie)
  print('Película agregada con éxito')


print('SISTEMA DE LÍBRERIA')
print('Bienvenido')

while True:
  menu_option = menu()
  
  if menu_option == 1:
    selected_material = material_type()
    if selected_material == 1:
      add_book()
    elif selected_material == 2:
      add_magazine()
    elif selected_material == 3:
      add_movie()
  
  elif menu_option == 2:
    storage.show_materials()
    
  elif menu_option == 3:
    storage.search_material()

  elif menu_option == 4:
    print(' \nHasta pronto')
    break
