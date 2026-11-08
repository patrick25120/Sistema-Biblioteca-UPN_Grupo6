# IMPORTACION DE MODULOS
# Se importan las funciones necesarias para integrar
# la gestion de libros, prestamos y ordenamiento.

from acceso import iniciar_sesion
from gestion_libros import (
    registrar_libro,
    mostrar_libros,
    buscar_libro,
    modificar_libro,
    eliminar_libro
)
from gestion_prestamos import (
    registrar_prestamo,
    registrar_devolucion,
    mostrar_prestamos,
    mostrar_mis_prestamos
)
from ordenamiento import ordenar_burbuja, ordenar_seleccion

# MENU DEL ESTUDIANTE
# Permite consultar libros, solicitar prestamos
# y realizar devoluciones.

def menu_estudiante(libros, prestamos, codigo):
    while True:
        print("\n===== MENU DEL ESTUDIANTE =====")
        print("1. Mostrar libros")
        print("2. Solicitar prestamo")
        print("3. Mostrar mis prestamos")
        print("4. Devolver libro")
        print("5. Salir")

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            mostrar_libros(libros)
        elif opcion == "2":
            registrar_prestamo(libros, prestamos, codigo)
        elif opcion == "3":
            mostrar_mis_prestamos(prestamos, codigo)
        elif opcion == "4":
            registrar_devolucion(libros, prestamos)
        elif opcion == "5":
            print("Sesion de estudiante finalizada.")
            break
        else:
            print("Opcion no valida.")

# MENU DEL BIBLIOTECARIO
# Permite administrar libros, prestamos,
# devoluciones y metodos de ordenamiento.

def menu_bibliotecario(libros, prestamos):
    while True:
        print("\n===== MENU DEL BIBLIOTECARIO =====")
        print("1. Registrar libro")
        print("2. Mostrar libros")
        print("3. Buscar libro")
        print("4. Modificar libro")
        print("5. Eliminar libro")
        print("6. Registrar devolucion")
        print("7. Mostrar prestamos")
        print("8. Ordenar por burbuja")
        print("9. Ordenar por seleccion")
        print("10. Salir")

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            registrar_libro(libros)
        elif opcion == "2":
            mostrar_libros(libros)
        elif opcion == "3":
            buscar_libro(libros)
        elif opcion == "4":
            modificar_libro(libros)
        elif opcion == "5":
            eliminar_libro(libros)
        elif opcion == "6":
            registrar_devolucion(libros, prestamos)
        elif opcion == "7":
            mostrar_prestamos(prestamos)
        elif opcion == "8":
            ordenar_burbuja(libros)
            mostrar_libros(libros)
        elif opcion == "9":
            ordenar_seleccion(libros)
            mostrar_libros(libros)
        elif opcion == "10":
            print("Sesion de bibliotecario finalizada.")
            break
        else:
            print("Opcion no valida.")

# INICIO E INTEGRACION DEL SISTEMA
# Inicializa los libros y prestamos y conecta
# el acceso con los menus correspondientes.

def iniciar_sistema():

    # Lista inicial de cinco libros disponibles.
    libros = [
        {
            "codigo": "L001",
            "titulo": "Don Quijote de la Mancha",
            "autor": "Miguel de Cervantes",
            "estado": "Disponible"
        },
        {
            "codigo": "L002",
            "titulo": "Cien años de soledad",
            "autor": "Gabriel Garcia Marquez",
            "estado": "Disponible"
        },
        {
            "codigo": "L003",
            "titulo": "El principito",
            "autor": "Antoine de Saint-Exupery",
            "estado": "Disponible"
        },
        {
            "codigo": "L004",
            "titulo": "La ciudad y los perros",
            "autor": "Mario Vargas Llosa",
            "estado": "Disponible"
        },
        {
            "codigo": "L005",
            "titulo": "Orgullo y prejuicio",
            "autor": "Jane Austen",
            "estado": "Disponible"
        }
    ]

    # Lista donde se almacenan los prestamos.
    prestamos = []

    # Bucle principal para permitir nuevas sesiones.
    while True:

        # Verificacion del tipo de usuario y codigo de acceso.
        tipo_usuario, codigo = iniciar_sesion()

        # Acceso al menu correspondiente segun el usuario.
        if tipo_usuario == "estudiante":
            menu_estudiante(libros, prestamos, codigo)
        else:
            menu_bibliotecario(libros, prestamos)

        # Consulta para continuar utilizando el sistema.
        respuesta = input("\nDesea utilizar el programa nuevamente? (S/N): ")
        respuesta = respuesta.upper()

        if respuesta != "S":
            print("Gracias por utilizar el sistema de biblioteca.")
            break
