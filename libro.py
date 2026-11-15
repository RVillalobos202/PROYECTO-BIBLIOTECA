class Libro:
    def __init__(self, codigo, titulo, autor, anio_publicacion, estado):
        self.__codigo = codigo
        self.__titulo = titulo
        self.__autor = autor
        self.__anio_publicacion = anio_publicacion
       
        if estado not in ["Disponible", "Prestado"]:
            raise ValueError("El estado debe ser 'Disponible' o 'Prestado'")  #ValueError para validar el estado 
        self.__estado = estado   

    @property
    def codigo(self):
        return self.__codigo

    @property
    def titulo(self):  
        return self.__titulo

    @property
    def autor(self):    
        return self.__autor

    @property
    def anio_publicacion(self):
        return self.__anio_publicacion

    @property
    def estado(self):
        return self.__estado

    def mostrar(self):
        print(f"Código del libro: {self.__codigo}") 
        print(f"Título del libro: {self.__titulo}")
        print(f"Autor del libro: {self.__autor}")
        print(f"Año de publicación: {self.__anio_publicacion}")
        print(f"Estado: {self.__estado}")

    def cambiar_estado(self, nuevo_estado):
        if nuevo_estado not in ["Disponible", "Prestado"]:
            raise ValueError("El estado debe ser 'Disponible' o 'Prestado'")
        self.__estado = nuevo_estado

    def prestar(self):
        self.cambiar_estado("Prestado")
    
    def devolver(self):
        self.cambiar_estado("Disponible")

    def consultar_codigo(self):
        return self.__codigo
    
    def consultar_estado(self):
        return self.__estado