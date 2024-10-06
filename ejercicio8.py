class ListaDeTareas:
    def __init__(self):
        # Inicializa la lista de tareas vacía
        self.tareas = []

    def agregar_tarea(self, tarea):
        # Agrega una tarea a la lista de tareas
        self.tareas.append(tarea)
        print(f"La tarea '{tarea}' ha sido agregada a la lista de tareas.")

    def eliminar_tarea(self, tarea):
        # Elimina una tarea de la lista si está presente
        if tarea in self.tareas:
            self.tareas.remove(tarea)
            print(f"La tarea '{tarea}' ha sido eliminada de la lista de tareas.")
        else:
            print(f"La tarea '{tarea}' no se encuentra en la lista de tareas.")

    def mostrar_tareas(self):
        # Muestra todas las tareas pendientes o indica que no hay tareas
        if self.tareas:
            print("Tareas pendientes:")
            for tarea in self.tareas:
                print(f"- {tarea}")
        else:
            print("No hay tareas pendientes.")

# Ejemplo de uso
lista_tareas = ListaDeTareas()
lista_tareas.mostrar_tareas()        # Muestra que no hay tareas pendientes
lista_tareas.agregar_tarea("Comprar leche")  # Agrega una tarea
lista_tareas.agregar_tarea("Hacer ejercicio")  # Agrega otra tarea
lista_tareas.mostrar_tareas()        # Muestra las tareas pendientes
lista_tareas.eliminar_tarea("Comprar leche")  # Elimina una tarea
lista_tareas.mostrar_tareas()        # Muestra las tareas restantes
lista_tareas.eliminar_tarea("Leer un libro")  # Intenta eliminar una tarea que no está en la lista
