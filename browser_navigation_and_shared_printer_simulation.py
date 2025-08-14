# 📌 Simulación del mecanismo adelante/atrás de un navegador web
# Utilizando pila y cadenas de texto:
# - Las palabras "adelante" y "atrás" desplazan en la historia de navegación.
# - Cualquier otro texto se interpreta como el nombre de una nueva web.
# - El programa muestra el nombre de la página actual en cada acción.


def interface():
  opcion = input(" \nBrowser\nPara ingresar una nueva dirección digite 1\nPara"
  "regresar ingrese 2\nPara ir hacia adelante ingrese 3: \n ")
  return opcion
 

history1 = ['inicio']  
history2 = []

while True:
  opcion = interface()
  
  match opcion:
    case '1':
      history1.append(input('Ingresar dirección: '))
      history2.clear()
      print(f'Bienvenido a {history1[-1]}')
    case '2':
      if len(history1) >= 2:
        history2.append(history1.pop())
        print(f'Bienvenido a {history1[-1]}')
      else:
        print('No es posible ir atrás')
    case '3':
      if len(history2) >= 1:
        history1.append(history2.pop())
        print(f'Bienvenido a {history1[-1]}')
      else:
        print('No es posible ir adelante')
    case _:
      print('Opción no valid
      a')
