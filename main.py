from datetime import datetime
from models.cliente import Cliente
from services.sala import Sala
from models.reserva import Reserva

cliente1 = Cliente("Nicol", "123", "nicol@email.com")
servicio1 = Sala("Sala VIP", 100, 20)

# caso correcto
reserva1 = Reserva(cliente1, servicio1, datetime.now())
print(reserva1.mostrar_reserva())

# caso con error
try:
    reserva_error = Reserva(None, servicio1, "fecha mala")
except:
    print("Error capturado correctamente")

# =========================================
# Autor: Yojan Esteban Ortega Benavides
# Casos de prueba y validaciones
# =========================================

from utils.validaciones import (
    validar_nombre,
    validar_cedula,
    validar_correo
)

print("\n===== VALIDACIONES =====")

try:
    validar_nombre("Yojan")
    print("Nombre válido")
except Exception as e:
    print(e)

try:
    validar_nombre("")
except Exception as e:
    print(e)

try:
    validar_cedula("123456")
    print("Cédula válida")
except Exception as e:
    print(e)

try:
    validar_cedula("12A45")
except Exception as e:
    print(e)

try:
    validar_correo("correo@gmail.com")
    print("Correo válido")
except Exception as e:
    print(e)

try:
    validar_correo("correo_malo")
except Exception as e:
    print(e)

# Caso con else y finally
try:
    validar_correo("yojan@gmail.com")
except Exception as e:
    print(e)
else:
    print("Correo procesado correctamente")
finally:
    print("Fin de validación")

# Prueba de cliente válido
try:
    cliente2 = Cliente("Yojan", "987654", "yojan@gmail.com")
    print(cliente2.mostrar_info())

    servicio2 = Sala("Sala Ejecutiva", 200, 30)

    reserva2 = Reserva(cliente2, servicio2, datetime.now())

    print(reserva2.mostrar_reserva())

except Exception as e:
    print(e)

# Prueba de segundo cliente válido
try:
    cliente3 = Cliente("Nicol", "456789", "nicol@gmail.com")
    print(cliente3.mostrar_info())
except Exception as e:
    print(e)

# Prueba de cliente inválido
try:
    cliente4 = Cliente("", "abc", "correo")
    print(cliente4.mostrar_info())
except Exception as e:
    print("Error en cliente inválido:", e)