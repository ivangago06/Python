import numpy as np # Se instaló la librería Numpy con la siguiente sentencia: pip install numpy en consola

# matriz simple

a = np.array([1,2,3])

print(a)
print(type(a))


# matriz de matrices

b = np.array([[1,2,3], [4,5,6]])
print(b)

c = np.array([[1.3,2.8,3.3], [4.4,5.1,6.3]])
d = np.array([[1,2,3], [4,5,6]], dtype=complex)

print(type(c))
print(type(d))

# funciones de matrices con Numpy

e = np.arange(4)
print('e=', e)


f = np.arange(12).reshape(2,6)
print('f=', f)

suma = b + c

print(suma)

# Multiplicación con Numpy

array1 = np.array([1,2,3])
array2 = np.array([1,2,3])

multiplicacion = array1 * array2

print("La multiplicación es: ", multiplicacion)

# traspuesta con Numpy

x=np.array([[1,2,3],[4,5,6],[7,8,9]])

y=np.transpose(x)

print("La tranpuesta de Numpy es: ", y)


# Esta es la manera de acceder a la posició deseada de una , empezando por el renlgon
print("\n",y)
print("La tranpuesta de Numpy es: \n", y[2][0]) 


print("y[0]=",y[0]) # aquí se imprime toda la row

print("y[:,0]=",y[:,0]) # aquí se imprime todo el col

print(y[0:2]) # con esto podemos imprimir fragmentos de la tupla

# Dado un número natural x mostrar su último digito.

num_natural = input("Ingrese un número natural: ")

if num_natural.isnumeric():
  print("El último digito es: ", num_natural[-1])



# Dado un número natural x contar el número de digitos que tiene
# Dado 3 numeros naturales, a,b y c, mostrar los multiplos de a, menores que b que no sean divisores de c


a = int(input("Ingresa a: "))
b = int(input("Ingresa b: "))
c = int(input("Ingresa c: "))


for i in range(1,a+1):
  resultado = a%i
  if resultado == 0 and resultado < b and c%i != 0:
    print("Numero que cumple las condiciones: ", i)
num_natural = input("Ingrese un número natural: ")

contador = 0
for digito in num_natural:
  contador+=1
print("La cantidad de digitos son: ", contador)



# Dada una matriz de n*m elementos calcular el promedio de cada fila y cada columna. mostrar en pantalla la matriz cargada y los promedios. y hacerlo con numpy

n = int(input("Ingresar el valor de n: "))
m = int(input("Ingresar el valor de m: "))

matriz = []

for fila in range(n):
  matriz.append([])
  for columna in range(m):
    numero = int(input("Ingresar numero: "))
    matriz[fila].append(numero)

c = 1
for fila in matriz:
  sumador = sum(fila)
  promedio = sumador // m    
  print(f"Promedio de la fila{c}:", promedio)
  c +=1

for columna in range(m):
  sumador = 0
  for fila in matriz:
    sumador +=fila[columna]
  promedio = sumador // n
  print(f"Promedio de la columna{columna+1}:", promedio)

for i in matriz:
  print(*i)


















# Pedir una lista de valores y ordenarla, validar si hay número repetidos.

longitud = input("Teclee la longitud que desee tener la lisa: ")

lista_desordenada = []
base = 1
while (base<=longitud): 
  elementos = int(input("Ingresa el elemento que se añadirá a la lista: ")) 
  lista_desordenada.append(elementos)  
  base+=1 

print("\nLista desordenada: ", lista_desordenada)
print("Lista ordenada: ", sorted(lista_desordenada))


# Dado un número natural sumar todos sus digitos y obtener la suma total. 

num_natural = int(input("Ingrese un número natural: "))

sumador = 0
while num_natural>0:
  digito = num_natural%10
  sumador+=digito
  num_natural=num_natural//10

print("El resultado de la suma es: ", sumador)


num_natural = input("Ingrese un número natural: ")

sumador = 0

for digito in num_natural:
  sumador+=int(digito)

print("El resultado de la suma es: ", sumador)






