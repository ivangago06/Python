# Realizar un CRUD (SELECT, UPDATE, INSERT Y DELETE) con menú selecionable con opción de salir, puede ser con MYSQL, SLQ o SQLITE3, se debe de entregar a mas tardar el 10 de julio

import mysql.connector

# Función para establecer la conexión con MySQL
def conectar():
    conexion = mysql.connector.connect(
        host="localhost",
        user="tu_usuario",
        password="tu_contraseña",
        database="tu_base_de_datos"
    )
    return conexion

# Función para mostrar el menú y obtener la opción seleccionada
def mostrar_menu():
    print("--- MENÚ ---")
    print("1. Seleccionar registros")
    print("2. Actualizar registro")
    print("3. Insertar registro")
    print("4. Eliminar registro")
    print("5. Salir")
    opcion = input("Seleccione una opción: ")
    return opcion

# Función para seleccionar registros
def seleccionar_registros():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM nombre_de_tabla")
    registros = cursor.fetchall()
    for registro in registros:
        print(registro)
    conexion.close()

# Función para actualizar un registro
def actualizar_registro():
    conexion = conectar()
    cursor = conexion.cursor()
    id = input("Ingrese el ID del registro a actualizar: ")
    nuevo_valor = input("Ingrese el nuevo valor: ")
    cursor.execute("UPDATE nombre_de_tabla SET columna = %s WHERE id = %s", (nuevo_valor, id))
    conexion.commit()
    print("Registro actualizado exitosamente.")
    conexion.close()

# Función para insertar un registro
def insertar_registro():
    conexion = conectar()
    cursor = conexion.cursor()
    valor1 = input("Ingrese el valor 1: ")
    valor2 = input("Ingrese el valor 2: ")
    cursor.execute("INSERT INTO nombre_de_tabla (columna1, columna2) VALUES (%s, %s)", (valor1, valor2))
    conexion.commit()
    print("Registro insertado exitosamente.")
    conexion.close()

# Función para eliminar un registro
def eliminar_registro():
    conexion = conectar()
    cursor = conexion.cursor()
    id = input("Ingrese el ID del registro a eliminar: ")
    cursor.execute("DELETE FROM nombre_de_tabla WHERE id = %s", (id,))
    conexion.commit()
    print("Registro eliminado exitosamente.")
    conexion.close()

# Función principal para ejecutar el programa
def ejecutar_programa():
    while True:
        opcion = mostrar_menu()

        if opcion == "1":
            seleccionar_registros()
        elif opcion == "2":
            actualizar_registro()
        elif opcion == "3":
            insertar_registro()
        elif opcion == "4":
            eliminar_registro()
        elif opcion == "5":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

# Ejecutar el programa
ejecutar_programa()
