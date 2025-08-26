# 📌 Determinar si un número es par o impar
# Este mini proyecto consiste en un programa que:
# Solicita al usuario que ingrese un número.
# Valida que la entrada sea un número válido.
# Determina si el número es par o impar usando el operador módulo (`%`).
# Muestra al usuario si el número ingresado es par o impar.

print("PAR O IMPAR")


def validate_prompt(prompt):
  while True:
    try:
      validated_prompt = int(input(prompt).strip())
      return validated_prompt
    except ValueError:
      print('Ingrese un número entero')


while True:
  validated_prompt = validate_prompt('Ingrese número: ')
  if validated_prompt % 2 == 0:
    print(f"El número {validated_prompt} es par")
  else:
    print(f"El número {validated_prompt} es impar")
