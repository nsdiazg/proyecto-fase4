from datetime import datetime
from utils.logger import registrar_error

# Clase que representa una reserva en el sistema
# Relaciona un cliente con un servicio en una fecha determinada
class Reserva:
    def __init__(self, cliente, servicio, fecha):
        # Atributos de la reserva
        self.cliente = cliente
        self.servicio = servicio
        self.fecha = fecha

        # Se validan los datos al momento de crear la reserva
        self.validar_datos()

    # Método que valida los datos de la reserva
    def validar_datos(self):
        try:
            # Verifica que el cliente exista
            if not self.cliente:
                raise ValueError("Cliente no puede estar vacío")

            # Verifica que el servicio exista
            if not self.servicio:
                raise ValueError("Servicio no puede estar vacío")

            # Verifica que la fecha sea válida
            if not isinstance(self.fecha, datetime):
                raise ValueError("Fecha inválida")

        except Exception as e:
            # Registra el error en el archivo de logs
            registrar_error(str(e))
            raise

    # Calcula el total de la reserva usando el servicio
    def calcular_total(self):
        return self.servicio.calcular_precio()

    # Muestra la información completa de la reserva
    def mostrar_reserva(self):
        return f"""
Cliente: {self.cliente.nombre}
Servicio: {self.servicio.mostrar_info()}
Fecha: {self.fecha}
Total: {round(self.calcular_total(), 2)}
"""