# Escrtibe un programa que al ingresar un numero, este sea el limite para que aparezca tu nombre, dicho también se tiene que ingresar.abs

numero = int(input("Numero de impresiones: "))
nombre = input("Ingresa tu nombre: ")

print("Con ciclo FOR:\n")

for repeticion in range(numero):
  print(nombre)


print("Con ciclo WHILE:\n")
contador=numero
while (contador>0):
  print(nombre)
  contador-=1

# Escribir un programa que pida el precio de un producto, se calcula el IVA del 21% e imprimir el valor final
precio = int(input("Ingresa el precio: "))
iva = 0.21
total = precio * iva + precio
print("El total con IVA aplicado es: ", total)

# Ingresar 2 numeros e imprimir el menor de ellos

n1 = int(input("Ingresa el numero 1: "))
n2 = int(input("Ingresa el numero 2: "))


if n1 <= n2:
  print("El numero menor es: ", n1)
else:
  print("El numero menor es: ", n2)
  
# Escribir un programa que pida al usuario un numero entero positivo  mostrar en la pantalla todos los numeros impares separados por "," a partir del 1

numero = int(input("Ingresa un numero: "))

if numero > 0:
  c = 1
  while (c<=numero):
    if c % 2 != 0:
      print(c, end=", ")
    c+=1
  """for c in range(1,numero+1):
    if c % 2 != 0:
      print(c, end=", ")"""
else:
  print("Ingresa un numero que sea mayor a 0: ")

  # Escribir un programa que pida al usuario un numero entero positivo  mostrar en la pantalla todos los numeros impares separados por "," a partir del numero ingresado hasta el 1

numero = int(input("Ingresa un numero: "))

if numero > 0:
  c = numero
  while (c >= 0):
    if c % 2 != 0:
      print(c, end=", ")
    c-=1
  """for c in range(1,numero+1):
    if c % 2 != 0:
      print(c, end=", ")"""
else:
  print("Ingresa un numero que sea mayor a 0: ")

  # Escribir un programa que pida al usuario un numero entero y que imprima un triángulo rectangulo

numero = int(input("Ingresa un numero: "))
triangulo = "*"
"""
for repeticion in range(numero):
  print(triangulo)
  triangulo+="*"
"""


contador = 0
while (contador<numero):
  print(triangulo)  
  triangulo+="*"
  contador+=1

  # Escribe un programa que muetre la tablade multiplcar que desees, lo anterior ingresando el valor

tabla = int(input("Ingresa la tabla de multiplicar que deseas imprimir: "))

contador = 0
for bucle in range(1,11):
  igual = tabla * bucle
  contador+=1
  print(tabla, " * ", contador, " = ", igual)


# escribir un programa que pregunte el nombre del usuario en la consola y después de capturado, mostrar en pantalla cuantas letras tiene el nombre, que letra es mayúscula y que posición tiene la letra mayúscula

nombre = input("Ingresa tu nombre: ")

indice=0
mayusculas=0
minusculas=0
while indice < len(nombre):
  letra = nombre[indice]
  if letra.isupper() == True:
    mayusculas +=1
  else:
    minusculas +=1
  indice += 1

print("Total mayúsculas:" , mayusculas)
print("Total minúsculas:" , minusculas)
print("Total de caracteres:" , indice, "\n")


for posicion, letra in enumerate(nombre):
  print("La posición es:", posicion, "pertenece a la letra: ", letra)
  
# Pedir al usuaio una palabra y mostrarla al reves

palabra = input("Ingresa cualquier palabra: ")

indice = len(palabra) - 1
while indice >=0:
  letra = palabra[indice]
  indice -=1

indice = len(palabra) - 1
for indice in range(indice,-1,-1):
  print(palabra[indice])


  # Ecribir un programa que pida al usuario ingresar un frase y una letra e imprimir cuantas veces aparece la letra en la frase.

frase = input("¿Cúal es la frase? ")
letra = input("Ingresa una letra: ")

indice = 0
contador = 0
'''
while indice < len(frase):
  if frase[indice] == letra:
    contador+=1    
  indice+=1
  
print("La letra ingresada aparece: ", contador, " veces")'''

for indice in frase:
  if indice==letra:
    contador+=1

print("La letra ingresada aparece: ", contador, " veces")
