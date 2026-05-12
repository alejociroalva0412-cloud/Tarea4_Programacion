# se inporta el sistema de registros de errores
import logging
# Convierte una clase en abstracta 
from abc import ABC, abstractmethod
# Inddica  donde se guardan los errores
logging.basicConfig(
    filename='errores_software_fj.log',
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
# Se crean las clases personalizadas que son errores creados 
class ErrorReserva(Exception):
    pass


class ClienteInvalido(Exception):
    pass


class ServicioNoDisponible(Exception):
    pass

# Clase cliente sera el molde para los objetos o clientes diferentes que tendremos Aqui trabajamos la encapsulación ya que protejemos los atributos 
class Cliente:

    def __init__(self, id_cliente, nombre, correo):

        if not nombre:
            raise ClienteInvalido(
                "El nombre no puede estar vacío"
            )

        if "@" not in correo:
            raise ClienteInvalido(
                "Correo inválido"
            )

        self.__id_cliente = id_cliente
        self.__nombre = nombre
        self.__correo = correo

# Utilizamos las propiedades para leer los atributos privados 
    @property
    def id_cliente(self):
        return self.__id_cliente

    @property
    def nombre(self):
        return self.__nombre

    @property
    def correo(self):
        return self.__correo

# Se crea la clase servicio como abtracta para que las clases hijas definan métodos obligatorios
class Servicio(ABC):

    def __init__(self, codigo, nombre, costo_base):

        self.codigo = codigo
        self.nombre = nombre
        self.costo_base = costo_base

    # Se obliga a las clases hijas a crear este método 
    @abstractmethod
    def calcular_costo(self, cantidad):
        pass

    @abstractmethod
    def descripcion(self):
        pass
  
# Aquí empezamos a trabajar la herenciay el polimorfismo. Está clase hija heredara los métodos de la clase servicio utilizando, en este caso obligatoriamente,  sus métodos
class AlquilerEquipos(Servicio):

    def calcular_costo(self, dias):

        return self.costo_base * dias

    def descripcion(self):

        return f"Servicio de alquiler: {self.nombre}"
    
# Creamos el segundo servicio  
class ReservaSalas(Servicio):

    def calcular_costo(self, horas):

        return self.costo_base * horas

    def descripcion(self):

        return f"Reserva de sala: {self.nombre}"

# Creamos el tercer servicio 
class AsesoriaEspecializada(Servicio):

    def calcular_costo(self, horas):

        return self.costo_base * horas

    def descripcion(self):

        return f"Asesoría especializada: {self.nombre}"
    
# Creamos la clase reserva donde unimos al cliente con los servicios y damos manejo a los datos y errores
 
class Reserva:

    def __init__(self, cliente, servicio, cantidad):

        self.cliente = cliente
        self.servicio = servicio
        self.cantidad = cantidad
        self.estado = "Pendiente"


    def confirmar_reserva(self):

        self.estado = "Confirmada"

        return "La reserva fue confirmada"
    
    
    def cancelar_reserva(self):

        self.estado = "Cancelada"

        return "La reserva fue cancelada"

    def procesar_reserva(self):

        try:

            if not isinstance(self.cantidad, (int, float)):
                raise TypeError("La cantidad debe ser numérica")

            if self.cantidad <= 0:
                raise ErrorReserva("La cantidad debe ser positiva")

            total = self.servicio.calcular_costo(self.cantidad)

        except TypeError as error:

            logging.error(error)

            self.estado = "Error"

            return f"ERROR DE TIPO: {error}"

        except ErrorReserva as error:

            logging.error(error)

            self.estado = "Error"

            return f"ERROR DE VALOR: {error}"

        else:

            self.estado = "Confirmada"

            return (
                f"Reserva confirmada\n"
                f"Cliente: {self.cliente.nombre}\n"
                f"Servicio: {self.servicio.nombre}\n"
                f"Total: ${total}"
            )

        finally:

            print("Proceso de reserva finalizado")

print("\n========== SOFTWARE FJ ==========\n")

# Operación 1, válida: Todo los datos ingresados correctamente
try:

    cliente1 = Cliente(
        "101",
        "Alejandro",
        "alejandro@gmail.com"
    )

    print("Cliente 1 registrado")

except Exception as e:

    logging.error(e)

    print(e)


# Operción 2, inválida: el nombre esta vacío pero el sistema sigue funcionando 
try:

    cliente2 = Cliente(
        "102",
        "",
        "correo@gmail.com"
    )

    print("Cliente 2 registrado")

except Exception as e:

    logging.error(e)

    print("Error:", e)


# Operción 3
try:

    equipo = AlquilerEquipos(
        "EQ01",
        "Computador Gamer",
        50000
    )

    print("Servicio de equipos creado")

except Exception as e:

    logging.error(e)

    print(e)

# Operación 4 
try:

    sala = ReservaSalas(
        "SL01",
        "Sala VIP",
        120000
    )

    print("Servicio de sala creado")

except Exception as e:

    logging.error(e)

    print(e)

# Operción 5
# Operación 5
try:

    asesoria = AsesoriaEspecializada(
        "AS01",
        "Python Avanzado",
        80000
    )

    print("Servicio de asesoría creado")

except Exception as e:

    logging.error(e)

    print(e)

# Operción 6 

try:

    reserva1 = Reserva(
        cliente1,
        equipo,
        3
    )

    print(reserva1.procesar_reserva())

except Exception as e:

    logging.error(e)

    print(e)

# Operación 7 

try:

    reserva2 = Reserva(
        cliente1,
        sala,
        -5
    )

    print(reserva2.procesar_reserva())

except Exception as e:

    logging.error(e)

    print(e)

# Operción 8
try:

    reserva3 = Reserva(
        cliente1,
        asesoria,
        "cinco"
    )

    print(reserva3.procesar_reserva())

except Exception as e:

    logging.error(e)

    print(e)

# Operción 9
try:

    reserva4 = Reserva(
        cliente1,
        asesoria,
        4
    )

    print(reserva4.procesar_reserva())

except Exception as e:

    logging.error(e)

    print(e)

#Operción 10 
try:

    print(reserva4.confirmar_reserva())

    print("Estado:",
          reserva4.estado)

except Exception as e:

    logging.error(e)

    print(e)
