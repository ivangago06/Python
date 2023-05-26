# Tipado dinámico

NOMBRE = "Gerardo"  # Para las constantes siempre serán en mayúsculas
EDAD = 35
SALDO = 74656.46868468
BOOL = True
ARREGLO = []
LLAVES = {}
PAREN = ()

# ESTRUCTURAS DE CONTROL

print("¿Que tipo de dato es este?",
      type(NOMBRE))  # Con esto vemos que tipo de variable es
print("¿Que tipo de dato es este?",
      type(EDAD))  # Con esto vemos que tipo de variable es
print("¿Que tipo de dato es este?",
      type(SALDO))  # Con esto vemos que tipo de variable es
print("¿Que tipo de dato es este?",
      type(BOOL))  # Con esto vemos que tipo de variable es
print("¿Que tipo de dato es este?",
      type(ARREGLO))  # Con esto vemos que tipo de variable es
print("¿Que tipo de dato es este?",
      type(LLAVES))  # Con esto vemos que tipo de variable es
print("¿Que tipo de dato es este?",
      type(PAREN))  # Con esto vemos que tipo de variable es

TEXTO1 = "Soy un texto"
TEXTO2 = 'Soy un texto'
TEXTO3 = """SOY UN TEXTO"""
TEXTO4 = '''SOY UN TEXTO'''

print(TEXTO1)
print(TEXTO2)
print(TEXTO3)
print(TEXTO4)

print("hol\n\t'a'")
print('hol"a"')

# Formateo de cadena

miNombre = "Ivan"
miApellido = "García"
miEdad = 35

print("Hola mi nombre es: {0} {1} {2}".format(miNombre, miApellido, miEdad))
print(
  f"Hola mi nombre es: {miNombre} y mi apellido es {miApellido} y mi edad es {miEdad}"
)

#concatenación

nombreCompleto = miNombre + " " + miApellido
print("Mi nombre completo es: " + nombreCompleto)
