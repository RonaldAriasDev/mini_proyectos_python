"""
Analiza palabras para propiedades específicas.

Prmite ingresar dos palabras y determinar:
- Si cada palabra es un 'palíndromo'.
- Si cada palabra es un 'isograma'.
- Si las palabras son 'anagramas' entre sí.
"""


def format_word(prompt):
    word = input(prompt).lower().strip()
    if word.isalpha():
        return word
    else:
        raise ValueError('La palabra debe contener solo letras')


def validate_word():
    while True:
        try:
            first_word = format_word('\nIngrese una palabra: ')
            second_word = format_word('Ingrese otra palabra: ')
            return first_word, second_word
        except ValueError as e:
            print(f'Ha ocurrido un error: {e}')
  

def is_palindrome(word):
    if word == word[::-1]:
        print(f'{word} es un palíndromo')
    else:
        print(f'{word} no es un palíndromo')

    
def is_isogram(word):
    my_set = set(word)
    
    if len(my_set) == len(word):
        print(f'{word} es un isograma')
    else:
        print(f'{word} no es un isograma')


def are_anagrams(word1, word2):
    list1 = sorted(list(word1))
    list2 = sorted(list(word2))
        
    if list1 == list2:
        print(f'{word1} y {word2} son anagramas')
    else:
        print(f'{word1} y {word2} no son anagramas')


def continue_or_exit():
    my_list = [
        'Ingrese una opción', 
        '1. Continuar', 
        '2. Salir: ', 
    ]
    while True:
        try:
            choice = int(input('\n' + '\n'.join(my_list)).strip())
            if choice == 1:
                return True
            elif choice == 2:
                print('Hasta pronto')
                return False
            else:
                print('Opción no valida')
          
        except ValueError:
            print('Ingrese un número entero')


print('ANALIZADOR DE PALABRAS')

while True:
    first_word, second_word = validate_word()
    is_palindrome(first_word)
    is_palindrome(second_word)
    is_isogram(first_word)
    is_isogram(second_word)
    are_anagrams(first_word, second_word)
    if not continue_or_exit():
        break
