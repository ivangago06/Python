# Investigar casos de uso laboral para una tupla de 1 solo elemento.

#Las tuplas son estructuras de datos inmutables en Python que se utilizan para almacenar un conjunto de elementos relacionados. Aunque las listas son más flexibles debido a su capacidad de modificación, las tuplas ofrecen algunas ventajas en ciertos escenarios, y su uso en el mundo laboral puede variar según el contexto. Aquí hay algunas formas comunes en las que se utilizan las tuplas en el ámbito laboral:

#Devolución múltiple de valores: Las tuplas son útiles cuando se necesita devolver múltiples valores de una función. Por ejemplo, una función que realiza algún cálculo puede devolver un resultado y algún estado auxiliar como una tupla, que luego puede ser desempaquetada en variables individuales para su posterior uso.

#Asignación de variables: Las tuplas permiten asignar múltiples valores a múltiples variables en una sola línea. Esto es especialmente útil cuando se trabaja con funciones que devuelven tuplas, ya que se puede desempaquetar los valores directamente en las variables correspondientes.

#Registro de datos: Las tuplas se pueden utilizar para representar registros de datos inmutables. Por ejemplo, en una base de datos, una tupla podría representar una fila con datos específicos, y cada elemento de la tupla podría corresponder a un campo en esa fila.

#Parámetros inmutables: En algunas situaciones, es necesario garantizar que los valores pasados a una función no puedan modificarse. Al utilizar tuplas en lugar de listas como parámetros, se asegura que los valores sean inmutables y no puedan cambiar accidentalmente dentro de la función.

#Uso en estructuras de datos más complejas: Las tuplas también se pueden utilizar como elementos dentro de estructuras de datos más complejas, como diccionarios o conjuntos. Por ejemplo, las tuplas pueden ser claves en un diccionario cuando se desea tener una clave compuesta.

#Recuerda que el uso de tuplas puede variar según el contexto y las necesidades específicas de tu entorno laboral. Es importante comprender las características y limitaciones de las tuplas para utilizarlas de manera efectiva en tus proyectos.


# Multiplicación y la traspuesta con Numpy
import numpy as np

matriz = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

transpuesta = np.transpose(matriz)
print(transpuesta)


matriz1 = np.array([[1, 2, 3],
                    [4, 5, 6]])

matriz2 = np.array([[7, 8],
                    [9, 10],
                    [11, 12]])

resultado = np.matmul(matriz1, matriz2)
print(resultado)
