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
