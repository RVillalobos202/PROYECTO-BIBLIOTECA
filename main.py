from biblioteca import Biblioteca
from funciones import mostrar_menu, pedir_opcion, pedir_libro, pedir_usuario


def ejecutar_programa():
    biblioteca = Biblioteca()

    while True:
        mostrar_menu()
        opcion = pedir_opcion()

        if opcion is None:
            continue

        if opcion == 1:
            biblioteca.agregar_libro(pedir_libro())

        elif opcion == 2:
            biblioteca.agregar_usuario(pedir_usuario())

        elif opcion == 3:
            biblioteca.mostrar_libros()

        elif opcion == 4:
            biblioteca.mostrar_usuarios()

        elif opcion == 5:
            carnet = input("Carnet del usuario: ").strip()
            codigo = input("Código del libro: ").strip()
            biblioteca.realizar_prestamo(carnet, codigo)

        elif opcion == 6:
            codigo = input("Código del libro a devolver: ").strip()
            biblioteca.devolver_libro(codigo)

        elif opcion == 7:
            biblioteca.mostrar_prestamos()

        elif opcion == 8:
            codigo = input("Código del libro a buscar: ").strip()
            libro = biblioteca.buscar_libro(codigo)
            if libro is None:
                print("No se encontró el libro.")
            else:
                libro.mostrar()

        elif opcion == 9:
            carnet = input("Carnet del usuario a buscar: ").strip()
            usuario = biblioteca.buscar_usuario(carnet)
            if usuario is None:
                print("No se encontró el usuario.")
            else:
                usuario.mostrar()

        elif opcion == 10:
            print("Gracias por utilizar el sistema de biblioteca.")
            break


if __name__ == "__main__":
    ejecutar_programa()