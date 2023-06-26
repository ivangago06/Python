class Persona:
    def __init__(self, nombre, edad, id):
        self.nombre = nombre
        self.edad = edad
        self.id = id

    def mostrar_edad(self):
        return self.edad
    
    def mayor_edad(self):
        if self.edad >= 18:
            return True
        else:
            return False
        
julian = Persona("Julian", 20, 125887)
print(julian.mostrar_edad())
print(julian.mayor_edad())