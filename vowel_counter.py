# CONTADOR DE VOCALES
# El programa solicita al usuario ingresar una palabra.
# Convierte la palabra a minúsculas y reemplaza las vocales acentuadas.
# Recorre cada letra e indica si es vocal o consonante.
# Al final, muestra la cantidad total de vocales en la palabra ingresada.

print("CONTADOR DE VOCALES")
word = input("Ingrese una palabra: ")
format_word = word.lower().strip().replace("á","a").replace("é", "e").replace("í","i").replace("ó", "o").replace("ú", "u")
vowels = ["a", "e", "i", "o", "u"]
vowel_count = 0

for letter in format_word:
  if letter in vowels:
    print(f"{letter}: es una vocal")
    vowel_count += 1
  else:
    print(f"{letter} es una consonante")

print(f" \nCantidad de vocales en {word}: {vowel_count}")
