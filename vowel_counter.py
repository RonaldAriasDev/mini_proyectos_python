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
    print(letter)

print(f"Cantidad de vocales en {word}: {vowel_count}")
