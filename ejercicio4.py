class Termostato:
    def __init__(self, temperatura_inicial):
        # Constructor que inicializa el atributo temperatura
        self.temperatura = temperatura_inicial

    def incrementar(self, grados):
        # Incrementa el valor de la temperatura en los grados especificados
        self.temperatura += grados
        print(f"La temperatura ha aumentado en {grados} grados. Temperatura actual: {self.temperatura}°C")

    def decrementar(self, grados):
        # Decrementa el valor de la temperatura en los grados especificados
        self.temperatura -= grados
        print(f"La temperatura ha disminuido en {grados} grados. Temperatura actual: {self.temperatura}°C")

    def mostrar_temperatura(self):
        # Muestra la temperatura actual del termostato
        print(f"Temperatura actual: {self.temperatura}°C")

# Ejemplo de uso
termostato = Termostato(20)  # Inicializa la temperatura a 20°C
termostato.mostrar_temperatura()  # Muestra la temperatura actual
termostato.incrementar(5)  # Aumenta la temperatura en 5 grados
termostato.decrementar(3)  # Disminuye la temperatura en 3 grados
termostato.mostrar_temperatura()  # Muestra la temperatura actual después de los cambios
