class Cafetera:
    def __init__(self, capacidad):
        # Inicializa la cafetera con capacidad máxima y nivel actual en 0
        self.capacidad = capacidad
        self.nivel_actual = 0

    def llenar_cafetera(self):
        # Llena la cafetera al máximo, es decir, establece el nivel actual igual a la capacidad
        self.nivel_actual = self.capacidad
        print(f"La cafetera ha sido llenada. Nivel actual: {self.nivel_actual} tazas.")

    def servir_cafe(self):
        # Disminuye el nivel de café en 1 si hay café disponible
        if self.nivel_actual > 0:
            self.nivel_actual -= 1
            print(f"Se ha servido una taza de café. Tazas restantes: {self.nivel_actual}")
        else:
            print("No hay café disponible para servir.")

    def mostrar_nivel(self):
        # Muestra cuántas tazas de café quedan disponibles
        print(f"Nivel actual de café: {self.nivel_actual} tazas.")

# Ejemplo de uso
cafetera = Cafetera(10)  # Capacidad máxima de 10 tazas
cafetera.mostrar_nivel()  # Muestra que la cafetera está vacía
cafetera.llenar_cafetera()  # Llena la cafetera al máximo
cafetera.servir_cafe()  # Sirve una taza de café
cafetera.servir_cafe()  # Sirve otra taza de café
cafetera.mostrar_nivel()  # Muestra cuántas tazas quedan
cafetera.servir_cafe()  # Sirve otra taza
