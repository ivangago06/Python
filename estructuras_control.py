# Ciclos en Python

# WHILE TRUE

while True:
  print("A")
  
numero = 1
while (numero<=10): # con los : se abre la sentencia del while  
  print(numero)
  numero+=1 # esto es lo mismo que numero = numero + 1
  
numero = 1
while (numero<10): # con los : se abre la sentencia del while  
  modulo = numero%2
  print(numero , "modulo: " , modulo)  
  if modulo==0:
    break  
  numero+=1 # esto es lo mismo que numero = numero + 1

numero = 1
while (numero<10): # con los : se abre la sentencia del while  
  algo = input("Algo: ")
  numero+=1

print("Time Out") 

# FOR

lista = [1,2,3,4,5] # Lista mutable
tupla = (1,2,3,4) #tupla inmutable
diccionario = {1:1, 2:2, 3:3} #referncia al key o indice 
cadena = "Hola texto" # cadena simple
texto = "hola" # cadena simple

for iterador in lista:
  print(iterador)


for numero in range(-5,6,5):
  print(numero)

for posicion, letra in enumerate(texto):
  print("La posición es: ", posicion)
  print("La letra es: ", letra)

for numero in range(30):
  print(numero)
  if numero==25:    
    break    

# ELIF

numero = int(input("Ingresa un numero: "))

if numero>5 and numero<10:
  cadena = "Es mayor que 5 y menor que 10"
  print(cadena)
elif numero==10:
  cadena = "Es igual 10"
  print(cadena)
elif numero==5:
  cadena = "Es igual que 5"
  print(cadena)
elif numero>5 and numero>10:
  cadena = "Es mayor que 5 y mayor que 10"
  print(cadena)
else:
  cadena = "Es menor que 5"
  print(cadena)

# escribir un programa que pregunte el nombre del usuario en la consola y después de capturado, mostrar en pantalla cuantas letras tiene el nombre, que letra es mayúscula y que posición tiene la letra mayúscula


  
