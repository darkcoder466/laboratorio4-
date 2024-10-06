class Libro:
    def __init__(self, titulo, autor):
        # Constructor que inicializa los atributos título, autor y disponible (True por defecto)
        self.titulo = titulo
        self.autor = autor
        self.disponible = True  # Por defecto, el libro está disponible

    def prestar(self):
        # Marca el libro como prestado (disponible = False) si está disponible
        if self.disponible:
            self.disponible = False
            print(f"El libro '{self.titulo}' ha sido prestado.")
        else:
            print(f"El libro '{self.titulo}' ya está prestado.")

    def devolver(self):
        # Marca el libro como disponible (disponible = True)
        if not self.disponible:
            self.disponible = True
            print(f"El libro '{self.titulo}' ha sido devuelto y está disponible.")
        else:
            print(f"El libro '{self.titulo}' ya está disponible.")

    def estado(self):
        # Muestra si el libro está disponible o prestado
        if self.disponible:
            print(f"El libro '{self.titulo}' está disponible.")
        else:
            print(f"El libro '{self.titulo}' está prestado.")

# Ejemplo de uso
libro = Libro("el lazarillo de tormes", "Anonimo")
libro.estado()      # Muestra si está disponible o prestado
libro.prestar()     # Presta el libro si está disponible
libro.estado()      # Muestra el estado del libro después de prestarlo
libro.devolver()    # Devuelve el libro y lo marca como disponible
libro.estado()      # Muestra el estado después de devolverlo
