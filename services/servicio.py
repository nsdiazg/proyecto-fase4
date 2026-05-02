from abc import ABC, abstractmethod

class Servicio(ABC):
    def __init__(self, nombre, precio):
        self._nombre = nombre
        self._precio = precio

    @abstractmethod
    def calcular_precio(self):
        pass

    def mostrar_info(self):
        return f"Servicio: {self._nombre}, Precio base: {self._precio}"