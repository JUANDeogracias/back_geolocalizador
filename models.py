class Dispositivo:
    def __init__(self, id, nombre, tipo, estado):
        self.id = id
        self.nombre = nombre
        self.tipo = tipo
        self.estado = estado

    def __str__(self):
        return f"Dispositivo {self.id} - {self.nombre} - {self.tipo} - {self.estado}"