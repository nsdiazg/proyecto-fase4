from utils.logger import registrar_error

# Clase que representa un cliente del sistema
class Cliente:
    def __init__(self, nombre, cedula, correo):
        # Se inicializa el cliente usando setters (incluyen validaciones)
        self.set_nombre(nombre)
        self.set_cedula(cedula)
        self.set_correo(correo)

    #  GETTERS 
    # Devuelven la información del cliente

    def get_nombre(self):
        return self.nombre

    def get_cedula(self):
        return self.cedula

    def get_correo(self):
        return self.correo

    #  SETTERS CON VALIDACIÓN 
    # Permiten asignar valores verificando que sean correctos

    def set_nombre(self, nombre):
        # Validar que el nombre no esté vacío
        if nombre == "":
            registrar_error("Nombre vacío")
            raise ValueError("El nombre no puede estar vacío")
        self.nombre = nombre

    def set_cedula(self, cedula):
        # Validar que la cédula sea numérica
        if not cedula.isdigit():
            registrar_error("Cédula inválida")
            raise ValueError("La cédula debe ser numérica")
        self.cedula = cedula

    def set_correo(self, correo):
        # Validar formato básico de correo
        if "@" not in correo:
            registrar_error("Correo inválido")
            raise ValueError("Correo inválido")
        self.correo = correo

    # Muestra la información completa del cliente
    def mostrar_info(self):
        return f"Nombre: {self.nombre}, Cédula: {self.cedula}, Correo: {self.correo}"