from prestamo import Prestamo
class Biblioteca:
    def __init__(self):
        self.__libros = []
        self.__usuarios = []
        self.__prestamos = []

    # Apartado de libros

    def agregar_libro(self, libro):
        if self.buscar_libro(libro.codigo) is not None:
            print("Ya existe un libro con ese código.")
            return False
        self.__libros.append(libro)
        print("Libro registrado.")
        return True

    def buscar_libro(self, codigo):
        for libro in self.__libros:
            if libro.codigo == codigo:
                return libro
        return None
    
    def eliminar_libro(self, codigo):
        libro = self.buscar_libro(codigo)
        if libro:
            self.__libros.remove(libro)
            print("Libro eliminado.")
            return True
        return False

    def mostrar_libros(self):
        for libro in self.__libros:
            print(f"Código: {libro.codigo}, Título: {libro.titulo}, Estado: {libro.estado}")


    # Apartado de usuarios

    def agregar_usuario(self, usuario):
        if self.buscar_usuario(usuario.carnet) is not None:
            print("Ya existe un usuario con ese carnet.")
            return False
        self.__usuarios.append(usuario)
        print("Usuario registrado.")
        return True

    def buscar_usuario(self, carnet):
        for usuario in self.__usuarios:
            if usuario.carnet == carnet:
                return usuario
        return None

    def mostrar_usuarios(self):
        for usuario in self.__usuarios:
            print(f"Carnet: {usuario.carnet}, Nombre: {usuario.nombre}")

    # Apartado de préstamos

    def realizar_prestamo(self, carnet, codigo):
        usuario = self.buscar_usuario(carnet)
        libro = self.buscar_libro(codigo)

        if usuario is None:
            print("Usuario no encontrado.")
            return False

        if libro is None:
            print("Libro no encontrado.")
            return False

        if libro.estado != "Disponible":
            print("libro no disponible para préstamo.")
            return False
        
        prestamo = Prestamo(libro, usuario)
        self.__prestamos.append(prestamo)
        usuario.agregar_prestamo(prestamo)
        libro.prestar()
        print("Préstamo realizado.")
        return True

    def devolver_libro(self, codigo):
        libro = self.buscar_libro(codigo)
        if libro is None:
            print("Libro no encontrado.")
            return False
        if libro.estado == "Disponible":
            print("El libro no está prestado.")
            return False

        for prestamo in self.__prestamos:
            if prestamo.libro.codigo == codigo:
                self.__prestamos.remove(prestamo)
                prestamo.usuario.quitar_prestamo(prestamo)
                libro.devolver()
                print("Libro devuelto.")
                return True
        print("Préstamo no encontrado.")
        return False

    def mostrar_prestamos(self):
        for prestamo in self.__prestamos:
            print(f"Usuario: {prestamo.usuario.nombre}, Libro: {prestamo.libro.titulo}")
    