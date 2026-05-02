from utils.logger import registrar_error

class Cliente:
    def __init__(self, nombre, cedula, correo):
        self.set_nombre(nombre)
        self.set_cedula(cedula)
        self.set_correo(correo)

    # getters
    def get_nombre(self):
        return self.nombre

    def get_cedula(self):
        return self.cedula

    def get_correo(self):
        return self.correo

    # setters con validación
    def set_nombre(self, nombre):
        if nombre == "":
            registrar_error("Nombre vacío")
            raise ValueError("El nombre no puede estar vacío")
        self.nombre = nombre

    def set_cedula(self, cedula):
        if not cedula.isdigit():
            registrar_error("Cédula inválida")
            raise ValueError("La cédula debe ser numérica")
        self.cedula = cedula

    def set_correo(self, correo):
        if "@" not in correo:
            registrar_error("Correo inválido")
            raise ValueError("Correo inválido")
        self.correo = correo

    def mostrar_info(self):
        return f"Nombre: {self.nombre}, Cédula: {self.cedula}, Correo: {self.correo}"