class Persona:
    def __init__(self, nombre, edad, genero):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
    def get_edad(self):
        return self.edad
    jenny = Persona(nombre = "Jenny", edad = 31, genero = "F")
    ivan = Persona(nombre = "Ivan", edad = 36, genero = "M")

    print(jenny.edad)
    print(ivan.edad)
    