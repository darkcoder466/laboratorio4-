class Temporizador:
    def __init__(self, tiempo_restante):
        # Inicializa el tiempo restante en segundos
        self.tiempo_restante = tiempo_restante
        self.pausado = False

    def iniciar(self):
        # Imprime un mensaje indicando que el temporizador ha sido iniciado
        self.pausado = False
        print(f"El temporizador ha sido iniciado con {self.tiempo_restante} segundos restantes.")

    def pausar(self):
        # Imprime un mensaje indicando que el temporizador ha sido pausado
        self.pausado = True
        print(f"El temporizador ha sido pausado. Tiempo restante: {self.tiempo_restante} segundos.")

    def mostrar_tiempo_restante(self):
        # Muestra el tiempo restante actual del temporizador
        if self.pausado:
            print(f"El temporizador está pausado. Tiempo restante: {self.tiempo_restante} segundos.")
        else:
            print(f"Tiempo restante: {self.tiempo_restante} segundos.")

# Ejemplo de uso
temporizador = Temporizador(120)  # Crea un temporizador con 120 segundos
temporizador.iniciar()             # Inicia el temporizador
temporizador.mostrar_tiempo_restante()  # Muestra el tiempo restante
temporizador.pausar()              # Pausa el temporizador
temporizador.mostrar_tiempo_restante()  # Muestra el tiempo restante mientras está pausado
