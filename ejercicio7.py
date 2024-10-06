class Biblioteca:
    def __init__(self):
        # Inicializa la lista de libros vacía
        self.libros = []

    def agregar_libro(self, libro):
        # Agrega un libro a la lista de libros
        self.libros.append(libro)
        print(f"El libro '{libro}' ha sido agregado a la biblioteca.")

    def eliminar_libro(self, libro):
        # Elimina un libro de la lista si está presente
        if libro in self.libros:
            self.libros.remove(libro)
            print(f"El libro '{libro}' ha sido eliminado de la biblioteca.")
        else:
            print(f"El libro '{libro}' no se encuentra en la biblioteca.")

    def mostrar_libros(self):
        # Muestra todos los libros en la biblioteca o indica que no hay libros
        if self.libros:
            print("Libros disponibles en la biblioteca:")
            for libro in self.libros:
                print(f"- {libro}")
        else:
            print("No hay libros en la biblioteca.")

# Ejemplo de uso
biblioteca = Biblioteca()
biblioteca.mostrar_libros()         # Muestra que no hay libros
biblioteca.agregar_libro("1984")    # Agrega el libro '1984'
biblioteca.agregar_libro("Don Quijote de la Mancha")  # Agrega otro libro
biblioteca.mostrar_libros()         # Muestra los libros en la biblioteca
biblioteca.eliminar_libro("1984")   # Elimina el libro '1984'
biblioteca.mostrar_libros()         # Muestra los libros restantes
biblioteca.eliminar_libro("El Hobbit")  # Intenta eliminar un libro que no está en la biblioteca
