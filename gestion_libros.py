from validaciones import validar_texto, validar_codigo_libro

#Registra un libro con su código, título, autor y estado inicial,
#y lo agrega a la lista de libros.
def registrar_libro(libros):
    codigo = validar_codigo_libro(libros)
    titulo = validar_texto("Ingrese el titulo: ")
    autor = validar_texto("Ingrese el autor: ")

    libro = {
        "codigo": codigo,
        "titulo": titulo,
        "autor": autor,
        "estado": "Disponible"
    }

    libros.append(libro)
    print("Libro registrado correctamente.")

#Muestra todos los libros registrados con sus datos y estado, 
#o informa si la lista está vacía.
def mostrar_libros(libros):
    if len(libros) == 0:
        print("No hay libros registrados.")
    else:
        print("\n===== LISTA DE LIBROS =====")

        for libro in libros:
            print("----------------------")
            print("Codigo:", libro["codigo"])
            print("Titulo:", libro["titulo"])
            print("Autor:", libro["autor"])
            print("Estado:", libro["estado"])

#Busca un libro por su código y muestra sus datos si lo encuentra; 
#de lo contrario, informa que no existe.
def buscar_libro(libros):
    codigo = input("Ingrese el codigo del libro: ").strip().upper()

    for libro in libros:
        if libro["codigo"] == codigo:
            print("Codigo:", libro["codigo"])
            print("Titulo:", libro["titulo"])
            print("Autor:", libro["autor"])
            print("Estado:", libro["estado"])
            return libro

    print("Libro no encontrado.")
    return None

#Busca un libro registrado y permite 
#modificar su título y autor si lo encuentra.
def modificar_libro(libros):
    libro = buscar_libro(libros)

    if libro is not None:
        libro["titulo"] = validar_texto("Ingrese el nuevo titulo: ")
        libro["autor"] = validar_texto("Ingrese el nuevo autor: ")

        print("Libro modificado correctamente.")

#Busca un libro y lo elimina si está disponible; 
#si está prestado, impide su eliminación.

def eliminar_libro(libros):
    libro = buscar_libro(libros)

    if libro is not None:
        if libro["estado"] == "Disponible":
            libros.remove(libro)
            print("Libro eliminado correctamente.")
        else:
            print("No se puede eliminar un libro prestado.")
