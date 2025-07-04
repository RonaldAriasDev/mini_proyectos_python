# Contador de vocales

print("CONTADOR DE VOCALES")

palabra = input("Ingrese una palabra: ")

palabra_formateada = palabra.lower().replace("á","a").replace("é", "e").replace("í","i").replace("ó", "o").replace("ú", "u")

vocales = ["a", "e", "i", "o", "u"]

x = 0

for i in palabra_formateada:
  if i in vocales:
    print(f"{i}: es una vocal")
    x += 1
  else:
    print(i)

print(f"cantidad de vocales en {palabra}: {x}")
