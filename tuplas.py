# Investigar casos de uso laboral para una tupla de 1 solo elemento.

# Multiplicación y la traspuesta con Numpy

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