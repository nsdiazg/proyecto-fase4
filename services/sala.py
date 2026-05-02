from services.servicio import Servicio

class Sala(Servicio):
    def __init__(self, nombre, precio, capacidad):
        super().__init__(nombre, precio)
        self.capacidad = capacidad

    def calcular_precio(self):
        return self._precio * 1.1

    def mostrar_info(self):
        return f"{super().mostrar_info()} | Capacidad: {self.capacidad}"