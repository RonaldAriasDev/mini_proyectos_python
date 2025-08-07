'''
Implementa dos clases que representen las estructuras de Pila y Cola (estudiadas en el ejercicio número 7 de la ruta de estudio)
Deben poder inicializarse y disponer de operaciones para añadir, eliminar, retornar el número de elementos e imprimir todo su contenido.
 '''
 
 
class Stack:
  def __init__(self, apps: list):
    self.apps = apps
  
  def add_app(self, app: str):
    self.apps.append(app)
  
  def remove_app(self):
    self.apps.pop()
  
  def count_apps(self):
    print(f'Cantidad de apps abiertas: {len(self.apps)}')
    
  def show_apps(self):
    print(f'Apps abiertas: {self.apps}')

recents_apps = Stack(['Acode', 'ChatGPT', 'GitHub'])
recents_apps.add_app('youtube')
recents_apps.remove_app()
recents_apps.count_apps()
recents_apps.show_apps()


class Queue:
  def __init__(self, nombres: list):
    self.nombres = nombres
  
  def show_queue(self):
    print(f'Clientes en fila: {self.nombres}')
    
  def count_customer(self):
    print(f'Cantidad de clientes en fila: {len(self.nombres)}')
  
  def add_customer(self, nombre: str):
    self.nombres.append(nombre)
    
  def remove_customer(self):
    self.nombres.pop(0)
    
turn = Queue(['Pedro', 'María', 'Juan'])
turn.add_customer('Rosa')
turn.remove_customer()
turn.count_customer()
turn.show_queue()