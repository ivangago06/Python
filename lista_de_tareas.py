class Lista_de_tareas: 
    lista_de_tareas = []
    def mostrar_tareas(self):
        return self.lista_de_tareas

    def agregar_tareas(self, tarea):
        self.lista_de_tareas.append(tarea)
        print("Tarea agregada con éxito")
    
    def quitar_tareas(self, tarea):
        if tarea in self.lista_de_tareas:
            self.lista_de_tareas.remove(tarea)
            print("Tarea elminada con éxito")
        else:
            print("No existe la tarea seleccionada")


cuaderno = Lista_de_tareas()
print(cuaderno.mostrar_tareas())
cuaderno.agregar_tareas("Salir a jugar")
cuaderno.agregar_tareas("Practicar Python")
cuaderno.agregar_tareas("Jugar Xbox")
cuaderno.agregar_tareas("Dormir")
print(cuaderno.mostrar_tareas())

cuaderno = Lista_de_tareas()
print(cuaderno.mostrar_tareas())
print(cuaderno.quitar_tareas("Practicar Python"))
print(cuaderno.mostrar_tareas())
print(cuaderno.quitar_tareas("Practicar Python"))

# Tarea---------------------------
# Crear una clase llamada Reveritr,donde se recibirá una lista de palabras, unir todas las palabras revertidas en un SOLO STRING, con 2 metdos (revertir y mostrar palabra) y el atributo será la lista de palabras.

class Reveritr:
    def __init__(self, lista_palabras):
        self.lista_palabras = lista_palabras

    def revertir(self):
        palabras_revertidas = [palabra[::-1] 
                               
        for palabra in self.lista_palabras]
        return ''.join(palabras_revertidas)

    def mostrar_palabras(self):
        return self.lista_palabras

lista = []
while True:    
    string = input("Ingresa un string (o presiona Enter para salir): ")    
    if string == "":
        break 
    lista.append(string) 
  
reveritr = Reveritr(lista)

# Imprimir la lista original de palabras
print("Lista de palabras:", reveritr.mostrar_palabras())
# Revertir y unir las palabras en un solo STRING
resultado = reveritr.revertir()
print("Palabras revertidas:", resultado)