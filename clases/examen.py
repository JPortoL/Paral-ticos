
import datetime


class Examen:
    def __init__(self, nombre: str, tipo: str, fecha_creacion: datetime, paciente: int,
                 estado: str, clinico_id: str, id: int = None, interpretacion: str = None,
                 fecha_interpretacion: datetime = None, resultado_id: int = None):
        self.id =  id
        self.nombre = nombre
        self.tipo = tipo
        self.fecha_creacion = fecha_creacion
        self.fecha_interpretacion = fecha_interpretacion
        self.paciente = paciente
        self.resultado_id = resultado_id
        self.interpretacion = interpretacion
        self.estado = estado
        self.clinico_id = clinico_id

    def __str__(self):
        return f'{self.id}, {self.nombre}, {self.tipo}, {self.fecha}, {self.paciente}, {self.resultado_id}, {self.interpretacion}'
    
    def crear(self):
        return f'INSERT INTO examen(nombre, tipo, fecha, paciente, resultado_id, interpretacion, estado)"\
                " VALUES ("{self.nombre}", "{self.tipo}", "{self.fecha_creacion}", "{self.fecha_interpretacion}", "{self.paciente}", "{self.interpretacion}")'

    def registrar_resultado_id(self, resultado_id):
        return f'UPDATE examen SET resultado_id = "{resultado_id}" WHERE id = {self.id}'
    
    def registrar_interpretacion(self, interpretacion):
        return f'UPDATE examen SET interpretacion = "{interpretacion}" WHERE id = {self.id}'
    
    def cambiar_estado(self, estado):
        return f'UPDATE examen SET estado = "{estado}" WHERE id = {self.id}'
    
    def consultar(self):
        return f'SELECT * FROM examen WHERE id = {self.id}'
    
    def consultar_paciente(self):
        return f'SELECT * FROM examen WHERE paciente = {self.paciente}'
    
    def cosultar_tipo(self):
        return f'SELECT * FROM examen WHERE tipo = "{self.tipo}"'