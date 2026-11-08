def ordenar_burbuja(libros):
    for i in range(len(libros) - 1):
        for j in range(len(libros) - i - 1):

            if libros[j]["titulo"].lower() > libros[j + 1]["titulo"].lower():
                libros[j], libros[j + 1] = libros[j + 1], libros[j]

    print("Libros ordenados por burbuja.")

def ordenar_seleccion(libros):
    for i in range(len(libros)):
        menor = i

        for j in range(i + 1, len(libros)):
            if libros[j]["titulo"].lower() < libros[menor]["titulo"].lower():
                menor = j

        libros[i], libros[menor] = libros[menor], libros[i]

    print("Libros ordenados por seleccion.")
