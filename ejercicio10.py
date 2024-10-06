class Album:
    def __init__(self):
        # Inicializa la lista de fotos vacía
        self.fotos = []

    def agregar_foto(self, foto):
        # Agrega una foto a la lista de fotos
        self.fotos.append(foto)
        print(f"La foto '{foto}' ha sido agregada al álbum.")

    def eliminar_foto(self, foto):
        # Elimina una foto de la lista si está presente
        if foto in self.fotos:
            self.fotos.remove(foto)
            print(f"La foto '{foto}' ha sido eliminada del álbum.")
        else:
            print(f"La foto '{foto}' no se encuentra en el álbum.")

    def mostrar_fotos(self):
        # Muestra todas las fotos en el álbum o indica que está vacío
        if self.fotos:
            print("Fotos en el álbum:")
            for foto in self.fotos:
                print(f"- {foto}")
        else:
            print("El álbum está vacío.")

# Ejemplo de uso
album = Album()
album.mostrar_fotos()           # Muestra que el álbum está vacío
album.agregar_foto("Vacaciones 2023")  # Agrega una foto
album.agregar_foto("Cumpleaños")        # Agrega otra foto
album.mostrar_fotos()           # Muestra las fotos en el álbum
album.eliminar_foto("Vacaciones 2023") # Elimina una foto
album.mostrar_fotos()           # Muestra las fotos restantes
album.eliminar_foto("Boda")     # Intenta eliminar una foto que no está en el álbum
