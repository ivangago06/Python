lista = [1,2,3,4,"hola",2.4,True,False]
tamano = len(lista)

print("Imprimir lista ", lista)

print("El último elemento de la lista es: ", lista[len(lista)-1])

print("Slicing, último elemento: ", lista[-1])

print("Slicing, primer elemento: ", lista[-8])

print("Slicing, ver todos los elementos: ", lista[:])

print("Slicing, ver todos los elementos: ", lista[0:])

print("Slicing, ver todos los elementos: ", lista[0:8])

print("Slicing, ver elementos especificados: ", lista[2:5])

print("Slicing, dar vuelta a la lista: ", lista[::-1])

"""
texto = ["Hola", "mi", "nombre", "es", "Ivan"]

for palabra in texto:
  print(palabra+ "  ", end="")


for palabra in range(len(texto)):
  print(texto[palabra])
"""

lista_desordenada = [4,8,1,9,-8,-4,10,1]

print(lista_desordenada)

lista_ordenada = sorted(lista_desordenada)

print(lista_ordenada)

lista_vacia = []
lista_vacia.append(20)
lista_vacia.append(-50)
lista_vacia.append(800)

print(lista_vacia)

lista_vacia.insert(2,4) # 1,4 posición, valor

print("Lista con insert", lista_vacia)


lista_vacia.extend([5,6,7])

print("Lista con extend", lista_vacia)

capturar = lista_vacia.pop(0)

print(lista_vacia)

del lista_vacia[0]

print(lista_vacia)

lista_vacia[-1] = 999

print(lista_vacia)

posicion = lista_vacia.index(999)

print(posicion)





