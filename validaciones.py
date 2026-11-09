def validar_texto(mensaje):
    # Bucle infinito para asegurar que el usuario ingrese un texto válido
    while True:
        # Solicita un texto mostrando el mensaje recibido y elimina los espacios en blanco a los extremos
        texto = input(mensaje).strip()

        # Verifica que el texto no esté vacío
        if texto != "":
            return texto  # Retorna el texto válido y finaliza la función

        # Si está vacío, muestra un mensaje de error y vuelve a solicitarlo
        print("Error: el campo no puede estar vacio.")


def validar_codigo_libro(libros):
    # Bucle infinito para validar que el código del libro sea único y no esté vacío
    while True:
        # Solicita el código, elimina espacios en blanco y lo convierte a mayúsculas
        codigo = input("Ingrese el codigo del libro: ").strip().upper()

        # Verifica si el campo quedó vacío
        if codigo == "":
            print("El codigo no puede estar vacio.")
        else:
            existe = False  # Bandera para rastrear si el código ya se encuentra registrado

            # Recorre la lista de libros existentes para comprobar duplicados
            for libro in libros:
                if libro["codigo"] == codigo:
                    existe = True

            # Si el código ya existe en el sistema, muestra un aviso y repite
            if existe:
                print("El codigo ya existe.")
            else:
                return codigo  # Retorna el código si es válido y no está repetido
