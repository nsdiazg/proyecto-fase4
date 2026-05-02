from services.servicio import Servicio

# Clase que representa el servicio de alquiler de equipos
# Hereda de la clase abstracta Servicio
class Equipo(Servicio):
    def __init__(self, nombre, precio, tipo):
        # Inicializa atributos heredados
        super().__init__(nombre, precio)
        # Tipo de equipo (ej: sonido, video, etc.)
        self.tipo = tipo

    # Implementación del método abstracto
    # Aplica un incremento del 20% al precio base
    def calcular_precio(self):
        return self._precio * 1.2

    # Muestra la información completa del servicio
    def mostrar_info(self):
        return f"{super().mostrar_info()} | Tipo: {self.tipo}"