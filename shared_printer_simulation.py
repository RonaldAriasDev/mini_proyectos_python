# 📌 Simulación del mecanismo de impresión de una impresora compartida
# Utilizando cola y cadenas de texto:
# - La palabra "imprimir" imprime el primer documento en la cola.
# - Cualquier otro texto se interpreta como el nombre de un nuevo documento que se agrega a la cola.
# - El programa muestra los documentos en cola y cuál se está imprimiendo en cada acción.

documents = []
documents.append(input('Documentos de notebook1:'))
documents.append(input('Documentos de notebook2:'))
print("Impresora")
while True:
  print(f'Documentos en cola: {documents}')
  option = input('Para imprimir ingrese 1\nPara salir ingrese 2: \n')
  if option == '1':
    print(f'Imprimiendo {documents[0]}')
    documents.pop(0)
  elif option == '2':
    print('Hasta pronto')
    break
  else:
    print('Opción invalida')