def validar_codigo_bibliotecario(codigo):
    codigo = codigo.upper()

    return (
        codigo.startswith("N0")
        and len(codigo) == 9
        and codigo[2:].isdigit()
    )

def validar_codigo_estudiante(codigo):
    codigo = codigo.upper()

    return (
        codigo.startswith("N00")
        and len(codigo) == 9
        and codigo[3:].isdigit()
    )

def iniciar_sesion():
    while True:
        print("\n===== ACCESO AL SISTEMA =====")
        print("1. Estudiante")
        print("2. Bibliotecario")

        opcion = input("Seleccione su tipo de usuario: ")

        if opcion == "1":
            codigo = input("Ingrese su codigo de estudiante: ").strip()

            if validar_codigo_estudiante(codigo):
                print("Acceso de estudiante correcto.")
                return "estudiante", codigo.upper()
            else:
                print("Codigo de estudiante incorrecto.")

        elif opcion == "2":
            codigo = input("Ingrese su codigo de bibliotecario: ").strip()

            if validar_codigo_bibliotecario(codigo):
                print("Acceso de bibliotecario correcto.")
                return "bibliotecario", codigo.upper()
            else:
                print("Codigo de bibliotecario incorrecto.")

        else:
            print("Opcion no valida.")
