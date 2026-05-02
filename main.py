from datetime import datetime
from models.cliente import Cliente
from services.sala import Sala
from models.reserva import Reserva

cliente1 = Cliente("Nicol", "123", "nicol@email.com")
servicio1 = Sala("Sala VIP", 100, 20)

#  caso correcto
reserva1 = Reserva(cliente1, servicio1, datetime.now())
print(reserva1.mostrar_reserva())

#  caso con error
try:
    reserva_error = Reserva(None, servicio1, "fecha mala")
except:
    print("Error capturado correctamente")