class Persona:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
        self.estado = "durmiendo"
    
    def dormir(self):
        if self.estado == "despierto":
            self.estado = "durmiendo"
        else:
            print(f"{self.nombre} ya esta durmiendo")
    def despertar(self):
        if self.estado == "durmiendo":
            self.estado = "despierto"
        else:
            print(f"{self.nombre} ya esta despierto.")
    def Estado(self):
        print(f"{self.nombre} de {self.edad} años esta {self.estado}.")

javier = Persona("javier",21)
javier.dormir()
javier.despertar()
javier.Estado()