from clases.examen import Examen
import datetime
from constantes.estadoExamen import EstadosExamen


class Clinico:
    def __init__(self, nombre: str, apellido: str, email: str, id: int = None):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.email = email

    def __str__(self):
        return f'{self.id} {self.nombre} {self.apellido}  {self.email}'
    
    def crear_examen(self, nombre: str, tipo: str, paciente: str) -> Examen:
        return Examen(nombre, tipo, datetime.datetime.now(), paciente, 
                      EstadosExamen.CREADO.value, self.id)
    


    