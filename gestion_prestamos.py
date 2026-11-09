def registrar_prestamo(libros, prestamos, codigo_estudiante):
    # Solicita al usuario el código del libro, elimina espacios en blanco y lo convierte a mayúsculas
    codigo = input("Ingrese el codigo del libro: ").strip().upper()

    # Recorre la lista de libros disponibles en el sistema
    for libro in libros:
        if libro["codigo"] == codigo:

            if libro["estado"] == "Disponible":
                libro["estado"] = "Prestado"

                prestamo = {
                    "codigo": codigo,
                    "estudiante": codigo_estudiante,
                    "estado": "Activo"
                }

                prestamos.append(prestamo)

                print("Prestamo registrado correctamente.")
                return

            print("El libro ya se encuentra prestado.")
            return

    print("Libro no encontrado.")

def registrar_devolucion(libros, prestamos):
    codigo = input("Ingrese el codigo del libro a devolver: ").strip().upper()

    for libro in libros:
        if libro["codigo"] == codigo:

            if libro["estado"] == "Prestado":
                libro["estado"] = "Disponible"

                for prestamo in prestamos:
                    if prestamo["codigo"] == codigo and prestamo["estado"] == "Activo":
                        prestamo["estado"] = "Devuelto"
                        break

                print("Devolucion registrada correctamente.")
                return

            print("El libro ya esta disponible.")
            return

    print("Libro no encontrado.")

def mostrar_prestamos(prestamos):
    if len(prestamos) == 0:
        print("No hay prestamos registrados.")
    else:
        print("\n===== HISTORIAL DE PRESTAMOS =====")

        for prestamo in prestamos:
            print("----------------------")
            print("Codigo del libro:", prestamo["codigo"])
            print("Codigo del estudiante:", prestamo["estudiante"])
            print("Estado:", prestamo["estado"])

def mostrar_mis_prestamos(prestamos, codigo_estudiante):
    encontrado = False

    for prestamo in prestamos:
        if prestamo["estudiante"] == codigo_estudiante:
            print("----------------------")
            print("Codigo del libro:", prestamo["codigo"])
            print("Estado:", prestamo["estado"])
            encontrado = True

    if not encontrado:
        print("No tienes prestamos registrados.")
