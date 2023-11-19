import datetime


class Examen:
    def __init__(self, nombre: str, tipo: str, fecha_creacion: datetime, paciente: int,
                 estado: str, clinico_id: int, id: int = None, interpretacion: str = None,
                 fecha_interpretacion: datetime = None, resultado_id: int = None):
        self.id = id
        self.nombre = nombre
        self.tipo = tipo
        self.fecha_creacion = fecha_creacion
        self.fecha_interpretacion = fecha_interpretacion
        self.paciente = paciente
        self.resultado_id = resultado_id
        self.interpretacion = interpretacion
        self.estado = estado
        self.clinico_id = clinico_id
