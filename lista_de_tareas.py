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
        palabras_revertidas = self.lista_palabras[::-1] 
                               
        for palabra in self.lista_palabras:
          return ' '.join(palabras_revertidas)

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

# Realiza un programa que somule una pelea con los guerreros Z en el cuál se van a tener las siguientes clases:
#Luchdor con atrubutos: nombre, kii, ssj, ataque, defensa, vida, con el metodo atacar y la clase batalla que se usará como menú, la cuál recibirá a los 2 luchadores y rebirá la batalla por turno.



class Luchador:
  def __init__(self, nombre, kii, ssj, ataque, defensa, vida):
    self.nombre = nombre
    self.kii = kii
    self.ataque = ataque
    self.defensa = defensa
    self.vida = vida
    print(f"El luchador {nombre} esta listo para pelear.")
  
  def atacar(self, enemigo):
    diferencia_ataque = self.ataque - enemigo.defensa
    enemigo.vida = enemigo.vida - diferencia_ataque
    print(
      f"{self.nombre} atacó a {enemigo.nombre} con {diferencia_ataque} de ataque"
    )
    print(f"La vida de  {enemigo.nombre} es {enemigo.vida}.")


class Batalla:
  turno = 1
  def __init__(self, luchador01, luchador02):
    self.luchador01 = luchador01
    self.luchador02 = luchador02

  def comenzar_batalla(self):
    while self.luchador01.vida > 0 and self.luchador02.vida > 0:
      if self.turno == 1:
        self.luchador01.atacar(self.luchador02)
        self.turno = 2
      else:
        self.luchador02.atacar(self.luchador01)
        self.turno = 1
      
      

goku = Luchador("Goku", 7000, True, 1000, 500, 1800)
majinbu = Luchador("majinbu", 7500, False, 700, 700, 1500)

#goku.atacar(majinbu)

Batalla(goku,majinbu).comenzar_batalla()