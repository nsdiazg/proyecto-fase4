# Sistema Integral de Gestión de Clientes, Servicios y Reservas

# Descripción del proyecto

Este proyecto fue desarrollado en Python utilizando Programación Orientada a Objetos (POO) para la empresa ficticia Software FJ.

El sistema permite gestionar clientes, servicios y reservas sin utilizar bases de datos, implementando toda la lógica mediante objetos, listas y manejo de archivos.

El proyecto fue diseñado para demostrar el uso correcto de:

- Abstracción
- Herencia
- Polimorfismo
- Encapsulación
- Manejo de excepciones
- Modularidad
- Validaciones
- Registro de logs
- Trabajo colaborativo con Git y GitHub

---

# Funcionalidades del sistema

El sistema permite:

- Registrar clientes
- Validar datos personales
- Gestionar servicios
- Crear reservas
- Calcular costos de servicios
- Registrar errores en logs
- Ejecutar validaciones y pruebas del sistema
- Continuar funcionando incluso cuando ocurren errores

---

# Arquitectura del proyecto

El proyecto está organizado en carpetas para mantener una estructura modular y ordenada.

# models

Contiene las clases principales del sistema:

- Cliente
- Reserva

# services

Contiene los diferentes servicios especializados:

- Sala
- Equipo
- Asesoria
- Servicio (clase abstracta)

# utils

Contiene herramientas auxiliares:

- validaciones.py
- excepciones.py
- logger.py

# logs

Contiene el archivo logs.txt donde se registran errores y eventos importantes del sistema.

---

# Conceptos de Programación Orientada a Objetos implementados

# Abstracción

Se implementó mediante la clase abstracta Servicio utilizando ABC y abstractmethod.

# Herencia

Las clases Sala, Equipo y Asesoria heredan de la clase abstracta Servicio.

# Polimorfismo

Cada servicio implementa su propia versión del método calcular_precio().

# Encapsulación

Se utilizaron atributos protegidos, getters y setters para controlar el acceso a los datos.

# Manejo de excepciones

Se implementaron excepciones personalizadas, validaciones y estructuras try/except para mantener la estabilidad del sistema.

---

# Manejo de excepciones y logs

El sistema implementa:

- try / except
- try / except / else / finally
- excepciones personalizadas
- validaciones robustas
- registro de errores en logs

Todos los errores detectados son almacenados automáticamente en:

logs/logs.txt

---

# Operaciones simuladas en el sistema

El proyecto incluye múltiples pruebas y simulaciones como:

- Clientes válidos
- Clientes inválidos
- Reservas válidas
- Reservas inválidas
- Correos válidos e inválidos
- Cédulas válidas e inválidas
- Validaciones de nombres
- Manejo de errores controlados

---

# Integrantes del proyecto

- Nicol
- Yojan

---

# Roles del equipo

# Nicol

- Líder del proyecto
- Organización inicial del sistema
- Creación de modelos y estructura principal
- Integración general del proyecto en GitHub

# Yojan

- Implementación de validaciones
- Creación de excepciones personalizadas
- Desarrollo de casos de prueba
- Apoyo en documentación y pruebas del sistema

---

# Tecnologías utilizadas

- Python
- Git
- GitHub
- Visual Studio Code

---

# Cómo ejecutar el proyecto

1. Abrir el proyecto en Visual Studio Code.
2. Abrir una terminal.
3. Ejecutar el siguiente comando:

```bash
python main.py