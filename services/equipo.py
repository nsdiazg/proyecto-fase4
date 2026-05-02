from services.servicio import Servicio

class Equipo(Servicio):
    def __init__(self, nombre, precio, tipo):
        super().__init__(nombre, precio)
        self.tipo = tipo

    def calcular_precio(self):
        return self._precio * 1.2

    def mostrar_info(self):
        return f"{super().mostrar_info()} | Tipo: {self.tipo}"