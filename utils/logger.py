import logging

logging.basicConfig(
    filename='logs/logs.txt',
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def registrar_error(mensaje):
    logging.error(mensaje)