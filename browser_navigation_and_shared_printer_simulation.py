"""
Utilizando la implementación de pila y cadenas de texto, simula el mecanismo adelante/atrás de un navegador web. 
Crea un programa en el que puedas navegar a una página o indicarle que te quieres desplazar adelante o atrás, mostrando en cada caso el nombre de la web.
Las palabras "adelante", "atrás" desencadenan esta acción, el resto se interpreta como el nombre de una nueva web.
"""

def interface():
  opcion = input(' \n\nBrowser\nPara ingresar una nueva dirección digite 1\nPara regresar ingrese 2\nPara ir hacia adelante ingrese 3: \n ')
  return opcion
 

history1 = ['inicio']        #
history2 = []                # 

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
      print('Opción no valida')


"""
Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una impresora compartida que recibe documentos y los imprime cuando así se le indica.
La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se interpretan como nombres de documentos
"""

documents = []
documents.append(input('Documentos de notebook1:'))
documents.append(input('Documentos de notebook2:'))
print("Impresora")
while True:
  print(f'Documentos en cola: {documents}')
  option = input('Para imprimir ingrese 1\nPara salir ingrese 2: \n')
  if option == '1':
    print(documents[0])
    documents.pop(0)
  elif option == '2':
    print('Hasta pronto')
    break
  else:
    print('Opción invalida')