'''
Una biblioteca necesita un sistema para administrar sus materiales.
Existen distintos tipos de materiales: libros, revistas y películas.
Cada material tiene título y año de publicación, pero además cada tipo de material tiene información extra:
Libro: nombre del autor y número de páginas.
Revista: número de edición y mes de publicación.
Película: director y duración en minutos.
El sistema debe permitir:
1. Registrar nuevos materiales.
2. Listar todos los materiales mostrando su información.
3. Permitir buscar materiales por título.
(Todos los materiales deben poder mostrar su información con un mismo método, pero cada tipo de material lo hará adaptado a sus propios datos).
'''


class Library:
  def __init__(self, title: str, year: int):
    self.title = title
    self.year = year
    self.materials = []
  
  def __str__(self):
    return f' \nTitulo: {self.title}\nAño de publicación: {self.year}'

  def add(self, material):
    self.materials.append(material)
  
  def show_materials(self):
    if len(self.materials) >= 1:
      for material in self.materials:
        print(material)
    else:
      print(f'No se ha registrado ningún material.')
      
  def search_material(self):
    title = format_text(input(' \nIngrese el título del material: '))
    for material in self.materials:
      if material.title == title:
        print(material)
        break
    else:
      print(f' \n{title} no está registrado')


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


storage = Library(None, None)


def menu():
  while True:
    try:
      menu_option = int(input(
        ' \nSeleccione una opción'
        '\n1. Registrar material'
        '\n2. Mostrar todos los materiales'
        '\n3. Buscar material por título'
        '\n4. Salir'))
      if menu_option in [1, 2, 3, 4]:
        return menu_option
      else:
        print(' \nSeleccione una opción valida')
    except ValueError:
        print(' \nDigite un número entero')


def material_type():
  while True:
    try:
      selected_material = int(input(
        ' \nSeleccione el tipo de material'
        '\n1. Libro'
        '\n2. Revista'
        '\n3. Pelicúla'))
      if selected_material in [1, 2, 3]:
        return selected_material
      else:
        print('Seleccione una opción valida')
    except ValueError:
      print('Digite un número entero')


def format_text(text: str):
  text = text.title().strip()
  return text


def format_number(prompt: str):
  while True:
    try:
      number = int(input(prompt))
      return number
    except ValueError:
      print('Digite un número entero')


def add_book():
  print(' \nIngrese los datos a continuación')
  title = format_text(input('Titulo: '))
  year = format_number('Año de publicación: ')
  author = format_text(input('Autor: '))
  number_pages = format_number('Número de páginas: ')
  new_book = Book(title, year, author, number_pages)
  storage.add(new_book)
  print('Libro agregado con éxito')


def add_magazine():
  print(' \nIngrese los datos a continuación')
  title = format_text(input('Titulo: '))
  year = format_number('Año de publicación: ')
  edition_number = format_number('Edicición n•: ')
  publication_month = format_text(input('Més de publicación: '))
  new_magazine = Magazine(title, year, edition_number, publication_month)
  storage.add(new_magazine)
  print('Revista agregada con éxito')

  
def add_movie():
  print(' \nIngrese los datos a continuación')
  title = format_text(input('Titulo: '))
  year = format_number('Año de publicación: ')
  director = format_text(input('Director: '))
  duration_minutes = format_number('Duración en minutos: ')
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
  