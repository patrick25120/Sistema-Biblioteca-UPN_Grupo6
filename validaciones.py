def validar_texto(mensaje):
    while True:
        texto = input(mensaje).strip()

        if texto != "":
            return texto

        print("Error: el campo no puede estar vacio.")


def validar_codigo_libro(libros):
    while True:
        codigo = input("Ingrese el codigo del libro: ").strip().upper()

        if codigo == "":
            print("El codigo no puede estar vacio.")
        else:
            existe = False

            for libro in libros:
                if libro["codigo"] == codigo:
                    existe = True

            if existe:
                print("El codigo ya existe.")
            else:
                return codigo
