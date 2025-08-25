# CONTADOR DE VOCALES
# El programa solicita al usuario ingresar una palabra.
# Reemplaza las vocales acentuadas y convierte la palabra a minúsculas.
# Recorre cada letra e indica si es vocal o consonante.
# Al final, muestra la cantidad total de vocales en la palabra ingresada.


def validate_prompt(prompt: str):
  while True:
    text = input(prompt).strip()
    if text.isalpha():
      return (
        text.replace('á','a')
            .replace('é', 'e')
            .replace('í','i')
            .replace('ó', 'o')
            .replace('ú', 'u')
            .lower()
            )
    else:
      print('Ingrese solo letras')


print("CONTADOR DE VOCALES")
vowels = ['a', 'e', 'i', 'o', 'u']

while True:
  validated_prompt = validate_prompt('' \nIngrese una palabra: ')
  if validated_prompt == ''
  vowels_count = 0
  
  for letter in validated_prompt:
    if letter in vowels:
      print(f'{letter}: es una vocal')
      vowels_count += 1
    else:
      print(f'{letter} es una consonante')

  print(f'Cantidad de vocales en {validated_prompt}: {vowels_count}')
