class CarritoDeCompras:
    def __init__(self):
        # Inicializa el atributo productos como una lista vacía
        self.productos = []

    def agregar_producto(self, producto):
        # Agrega un producto a la lista de productos
        self.productos.append(producto)
        print(f"Producto '{producto}' ha sido agregado al carrito.")

    def eliminar_producto(self, producto):
        # Elimina un producto de la lista de productos si está presente
        if producto in self.productos:
            self.productos.remove(producto)
            print(f"Producto '{producto}' ha sido eliminado del carrito.")
        else:
            print(f"El producto '{producto}' no está en el carrito.")

    def mostrar_productos(self):
        # Muestra los productos en el carrito o indica que está vacío si no hay productos
        if self.productos:
            print("Productos en el carrito:")
            for producto in self.productos:
                print(f"- {producto}")
        else:
            print("El carrito está vacío.")

# Ejemplo de uso
carrito = CarritoDeCompras()
carrito.mostrar_productos()        # Muestra que el carrito está vacío
carrito.agregar_producto("Manzanas")
carrito.agregar_producto("Leche")
carrito.mostrar_productos()        # Muestra los productos en el carrito
carrito.eliminar_producto("Leche") 
carrito.mostrar_productos()        # Muestra los productos restantes
carrito.eliminar_producto("Pan")   # Intenta eliminar un producto que no está en el carrito
