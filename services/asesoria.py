from services.servicio import Servicio

# Clase que representa el servicio de asesoría
# Hereda de la clase abstracta Servicio
class Asesoria(Servicio):
    def __init__(self, nombre, precio, horas):
        # Inicializa atributos heredados
        super().__init__(nombre, precio)
        # Número de horas de la asesoría
        self.horas = horas

    # Implementación del método abstracto
    # El precio total depende de la cantidad de horas
    def calcular_precio(self):
        return self._precio * self.horas

    # Muestra la información completa del servicio
    def mostrar_info(self):
        return f"{super().mostrar_info()} | Horas: {self.horas}"