from datetime import datetime
from utils.logger import registrar_error

class Reserva:
    def __init__(self, cliente, servicio, fecha):
        self.cliente = cliente
        self.servicio = servicio
        self.fecha = fecha

        self.validar_datos()

    def validar_datos(self):
        try:
            if not self.cliente:
                raise ValueError("Cliente no puede estar vacío")

            if not self.servicio:
                raise ValueError("Servicio no puede estar vacío")

            if not isinstance(self.fecha, datetime):
                raise ValueError("Fecha inválida")

        except Exception as e:
            registrar_error(str(e))
            raise

    def calcular_total(self):
        return self.servicio.calcular_precio()

    def mostrar_reserva(self):
        return f"""
Cliente: {self.cliente.nombre}
Servicio: {self.servicio.mostrar_info()}
Fecha: {self.fecha}
Total: {round(self.calcular_total(), 2)}
"""