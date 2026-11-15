from libro import Libro
from usuario import Usuario

def mostrar_menu():
    print("\n=== Menú de opciones ===")
    print("1. Registrar libro")
    print("2. Registrar usuario")
    print("3. Mostrar libros")
    print("4. Mostrar usuarios")
    print("5. Realizar préstamo")
    print("6. Devolver libro")
    print("7. Mostrar préstamos")
    print("8. Buscar libro")
    print("9. Buscar usuario")
    print("10. Salir")

def pedir_opcion():
    entrada = input("Ingrese una opción: ")
    if not entrada.isdigit():
        print("Opción inválida. Por favor, ingrese un número.")
        return None
    opcion = int(entrada)
    if opcion < 1 or opcion > 10:
        print("Opción inválida. Por favor, ingrese un número entre 1 y 10.")
        return None
    return opcion

def pedir_libro():
    codigo = input("codigo: ").strip()  # strip() para eliminar espacios en blanco al inicio y al final
    titulo = input("titulo: ").strip()
    autor = input("autor: ").strip()
    anio_publicacion = input("año de publicación: ").strip()
    return Libro(codigo, titulo, autor, anio_publicacion, "Disponible")

def pedir_usuario():
    carnet = input("carnet: ").strip()
    nombre = input("nombre: ").strip()
    correo = input("correo: ").strip()
    return Usuario(carnet, nombre, correo)