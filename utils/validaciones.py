import re

from utils.excepciones import (
    NombreInvalidoError,
    CedulaInvalidaError,
    CorreoInvalidoError
)


def validar_nombre(nombre):

    if nombre.strip() == "":
        raise NombreInvalidoError(
            "El nombre no puede estar vacío"
        )

    if len(nombre) < 3:
        raise NombreInvalidoError(
            "El nombre debe tener mínimo 3 caracteres"
        )

    return True


def validar_cedula(cedula):

    if not cedula.isdigit():
        raise CedulaInvalidaError(
            "La cédula debe contener solo números"
        )

    return True


def validar_correo(correo):

    patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'

    if not re.match(patron, correo):
        raise CorreoInvalidoError(
            "Correo inválido"
        )

    return True