from models.cliente import Cliente

try:
    cliente = Cliente("Nicol", "123456", "nsdiazg@correo.com")
    print(cliente.mostrar_info())
except Exception as e:
    print("Error:", e)