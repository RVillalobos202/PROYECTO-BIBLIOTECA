class Usuario:

    def __init__(self, carnet, nombre, correo):
        self.__carnet = carnet
        self.__nombre = nombre
        self.__correo = correo
        self.__libros_prestados = []  # Lista para almacenar los libros prestados por el usuario
    
    @property
    def carnet(self):
        return self.__carnet

    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def correo(self):
        return self.__correo
    
    @property
    def libros_prestados(self):
        return self.__libros_prestados

    def agregar_prestamo(self, prestamo):
        self.__libros_prestados.append(prestamo)

    def quitar_prestamo(self, prestamo):
        if prestamo in self.__libros_prestados:
            self.__libros_prestados.remove(prestamo)
        

    def mostrar(self):
        print(f"Carnet del usuario: {self.__carnet}")
        print(f"Nombre del usuario: {self.__nombre}")
        print(f"Correo del usuario: {self.__correo}")
        print("Libros prestados:")

        for prestamo in self.__libros_prestados:
            print(f" - Libro: {prestamo.libro.titulo}, Estado: {prestamo.libro.estado}")

    def consultar_carnet(self):
        return self.__carnet
    
    def consultar_nombre(self):
        return self.__nombre

    def consultar_correo(self):
        return self.__correo