from services.servicio import Servicio

# Clase que representa el servicio de alquiler de sala
# Hereda de la clase abstracta Servicio
class Sala(Servicio):
    def __init__(self, nombre, precio, capacidad):
        # Inicializa los atributos heredados
        super().__init__(nombre, precio)
        # Capacidad máxima de la sala
        self.capacidad = capacidad

    # Implementación del método abstracto
    # Aplica un incremento del 10% al precio base
    def calcular_precio(self):
        return self._precio * 1.1

    # Muestra la información completa del servicio
    def mostrar_info(self):
        return f"{super().mostrar_info()} | Capacidad: {self.capacidad}"