"""
 Crea un programa que analice dos palabras diferentes y que devuelva si son:
- Palíndromos: reconocer
- Anagramas: vela vale
- Isogramas: hola
 """
 
print("ANALIZADOR DE PALABRAS")
 

def show_options():
  user_choice = int(input("Para continuar ingrese 1. Para salir, 2: "))
  return user_choice


def format_input(word):
  word = word.lower().strip()
  if not word.isalpha():
    raise ValueError("La palabra debe contener solo letras")
  return word


def enter_word():
  first_word = format_input(input("Ingrese una palabra: "))
  second_word = format_input(input("Ingrese otra palabra: "))
  return first_word, second_word
  

def is_palindrome(first_word, second_word):
  if first_word == first_word[::-1]:
    print(f"{first_word} es un palíndromo")
  else:
    print(f"{first_word} no es un palíndromo")

  if second_word == second_word[::-1]:
    print(f"{second_word} es un palíndromo")
  else: 
    print(f"{second_word} no es un palíndromo")


def is_anagrams(first_word, second_word):
  first_list = sorted(list(first_word))
  second_list = sorted(list(second_word))
      
  if first_list == second_list:
    print(f"{first_word} y {second_word} son anagramas")
  else:
    print(f"{first_word} y {second_word} no son anagramas")
    
    
def is_isogram(first_word, second_word):
  first_set = set(first_word)
  second_set = set(second_word)
  
"""
Si la longitud de el conjunto y la cadena de texto son iguales, no se eliminó
ningún elemento de la cadena cuando se convirtio a conjunto, por tanto no
tiene elementos (letras) repetidos
"""
  if len(first_set) == len(first_word):
    print(f"{first_word} es un isograma")
  else:
    print(f"{first_word} no es un isograma")
    
  if len(second_set) == len(second_word):
    print(f"{second_word} es un isograma")
  else:
    print(f"{second_word} no es un isograma")


loop_control = 1
while loop_control == 1:
  try:
    user_choice = show_options()
  except ValueError:
    print("Ingrese un numero entero")
    continue 
  
  if user_choice == 1:
    try:
      first_word, second_word = enter_word()
    except ValueError as e:
      print(e)
      continue
    is_palindrome(first_word, second_word)
    is_anagrams(first_word, second_word)
    is_isogram(first_word, second_word)
  elif user_choice == 2:
    loop_control = 2
    print("Hasta pronto")
  else:
    print("Ingrese una opción valida")
