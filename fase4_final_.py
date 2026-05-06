import logging

# Configuración del archivo de errores (Log)
logging.basicConfig(
    filename='errores_software_fj.log',
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class Cliente:
    def __init__(self, id_cliente, nombre, correo):
        if not nombre or "@" not in correo:
            raise ValueError("Datos inválidos: Nombre vacío o correo sin formato @")
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.correo = correo

class Servicio:
    def __init__(self, codigo, tipo, costo_base):
        self.codigo = codigo
        self.tipo = tipo
        self.costo_base = costo_base
    def calcular_costo(self, cantidad):
        return self.costo_base * cantidad

class AlquilerEquipos(Servicio):
    pass

class ReservaSalas(Servicio):
    pass

class Reserva:
    def __init__(self, cliente, servicio, cantidad):
        self.cliente = cliente
        self.servicio = servicio
        self.cantidad = cantidad

    def procesar(self):
        try:
            if not isinstance(self.cantidad, (int, float)) or self.cantidad <= 0:
                raise ValueError("La cantidad debe ser un número positivo.")
            total = self.servicio.calcular_costo(self.cantidad)
            return f"ÉXITO: Cliente: {self.cliente.nombre} (ID: {self.cliente.id_cliente}) reservó {self.servicio.tipo}. Total: ${total:,.2f}"
        except Exception as e:
            logging.error(f"Fallo en reserva para {self.cliente.nombre}: {e}")
            return "ERROR CONTROLADO: No se pudo completar la reserva. (Ver log para detalles)"

# --- EJECUCIÓN ---
pc_gamer = AlquilerEquipos("EQ01", "Computador Gamer", 50000)
sala_vp = ReservaSalas("SL01", "Sala Video-Presencial", 120000)

try:
    c1 = Cliente("101", "Robinson Loaiza", "robinson@unad.edu.co")
    print(Reserva(c1, pc_gamer, 3).procesar())
    print(Reserva(c1, sala_vp, 2).procesar())
    print(Reserva(c1, pc_gamer, -5).procesar())
    print(Reserva(c1, pc_gamer, "tres").procesar())
except Exception as e:
    print(f"Error: {e}")