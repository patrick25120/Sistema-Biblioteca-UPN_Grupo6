def registrar_prestamo(libros, prestamos, codigo_estudiante):
    # Solicita al usuario el código del libro, elimina espacios en blanco y lo convierte a mayúsculas
    codigo = input("Ingrese el codigo del libro: ").strip().upper()

    # Recorre la lista de libros disponibles en el sistema
    for libro in libros:
        if libro["codigo"] == codigo:

            # Verifica si el libro está disponible para ser prestado
            if libro["estado"] == "Disponible":
                libro["estado"] = "Prestado"  # Actualiza el estado del libro

                # Crea un diccionario con la información del nuevo préstamo
                prestamo = {
                    "codigo": codigo,
                    "estudiante": codigo_estudiante,
                    "estado": "Activo"
                }

                # Añade el préstamo a la lista general de préstamos
                prestamos.append(prestamo)

                print("Prestamo registrado correctamente.")
                return

            # Si el libro ya fue prestado previamente
            print("El libro ya se encuentra prestado.")
            return

    # Si recorre todo el ciclo y no encuentra el código del libro
    print("Libro no encontrado.")

def registrar_devolucion(libros, prestamos):
    # Solicita el código del libro que se desea devolver
    codigo = input("Ingrese el codigo del libro a devolver: ").strip().upper()

    # Busca el libro en la lista
    for libro in libros:
        if libro["codigo"] == codigo:

            # Verifica que el libro realmente figure como prestado
            if libro["estado"] == "Prestado":
                libro["estado"] = "Disponible"  # Cambia su estado a disponible

                # Busca el registro activo de ese préstamo para actualizarlo
                for prestamo in prestamos:
                    if prestamo["codigo"] == codigo and prestamo["estado"] == "Activo":
                        prestamo["estado"] = "Devuelto"
                        break  # Sale del ciclo una vez actualizado

                print("Devolucion registrada correctamente.")
                return

            # Si el libro ya estaba disponible
            print("El libro ya esta disponible.")
            return

    # Si no se encuentra el libro ingresado
    print("Libro no encontrado.")

def mostrar_prestamos(prestamos):
    # Verifica si la lista de préstamos está vacía
    if len(prestamos) == 0:
        print("No hay prestamos registrados.")
    else:
        print("\n===== HISTORIAL DE PRESTAMOS =====")

        # Recorre y muestra la información de cada préstamo registrado
        for prestamo in prestamos:
            print("----------------------")
            print("Codigo del libro:", prestamo["codigo"])
            print("Codigo del estudiante:", prestamo["estudiante"])
            print("Estado:", prestamo["estado"])

def mostrar_mis_prestamos(prestamos, codigo_estudiante):
    # Bandera para saber si se encontraron préstamos del estudiante
    encontrado = False

    # Recorre todos los préstamos buscando los que coincidan con el estudiante
    for prestamo in prestamos:
        if prestamo["estudiante"] == codigo_estudiante:
            print("----------------------")
            print("Codigo del libro:", prestamo["codigo"])
            print("Estado:", prestamo["estado"])
            encontrado = True

    # Si no se encontró ningún préstamo asociado al estudiante
    if not encontrado:
        print("No tienes prestamos registrados.")
