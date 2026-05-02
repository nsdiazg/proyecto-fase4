from services.servicio import Servicio

class Asesoria(Servicio):
    def __init__(self, nombre, precio, horas):
        super().__init__(nombre, precio)
        self.horas = horas

    def calcular_precio(self):
        return self._precio * self.horas

    def mostrar_info(self):
        return f"{super().mostrar_info()} | Horas: {self.horas}"
