from abc import ABC, abstractmethod

# Clase abstracta que representa un servicio general
# No se puede instanciar directamente, solo sirve como base
class Servicio(ABC):
    def __init__(self, nombre, precio):
        # Atributos protegidos del servicio
        self._nombre = nombre
        self._precio = precio

    # Método abstracto que obliga a las clases hijas a implementarlo
    @abstractmethod
    def calcular_precio(self):
        pass

    # Método que muestra la información básica del servicio
    def mostrar_info(self):
        return f"Servicio: {self._nombre}, Precio base: {self._precio}"