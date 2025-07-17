"""
 Crea un programa que analice dos palabras diferentes y que devuelva si son:
- Palíndromos: reconocer
- Anagramas: RONALD ARNOLD
- Isogramas: SOL LUNA
 """
 
print("ANALIZADOR DE PALABRAS")
 
 
def format_input(word):
  return word.lower().strip()


loop_control = 1
while loop_control == 1:
  continue_exit = int(input("Para continuar ingrese 1. Para salir, 2: "))
  
  if continue_exit == 1:
    first_word = format_input(input("Ingrese una palabra: "))
    second_word = format_input(input("Ingrese otra palabra: "))
    
    if first_word == first_word[::-1]:
      print(f"{first_word} es un palíndromo")
    else:
      print(f"{first_word} no es un palíndromo")
      
    if second_word == second_word[::-1]:
      print(f"{second_word} es un palíndromo")
    else: 
      print(f"{second_word} no es un palíndromo")
    
    first_list = sorted(list(first_word))
    second_list = sorted(list(second_word))
    
    if first_list == second_list:
      print(f"{first_word} y {second_word} son anagramas")
    else:
      print(f"{first_word} y {second_word} no son anagramas")
    
    first_set = set(first_word)
    second_set = set(second_word)
    
    # si la longitud de el conjunto y la cadena de texto son iguales, no se eliminó ningún elemento de la cadena cuando se convirtio a conjunto, por tanto no tiene elementos (letras) repetidos
    if len(first_set) == len(first_word):
      print(f"{first_word} es un isograma")
    else:
      print(f"{first_word} no es un isograma")
      
    if len(second_set) == len(second_word):
      print(f"{second_word} es un isograma")
    else:
      print(f"{second_word} no es un isograma")
  elif continue_exit == 2:
    loop_control = 2
    print("Hasta pronto")