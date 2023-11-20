import datetime
from fastapi import HTTPException

from clases.examen import Examen
from clases.resultado import Resultado
from clases.tipoExamen import TipoExamen
from constantes.estadoExamen import EstadosExamen


class Clinico:
    def __init__(self, nombre: str, apellido: str, email: str, id: int = None):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.email = email

    def __str__(self):
        return f'{self.id} {self.nombre} {self.apellido}  {self.email}'

    def crear_examen(self, tipo_examen: TipoExamen, paciente_id: int) -> Examen:
        return Examen(tipo_examen.id, datetime.datetime.now(), paciente_id,
                      EstadosExamen.CREADO.value, self.id)

    def registrar_resultado(
            self,
            tipo_examen: TipoExamen,
            limite_superior: float,
            limite_inferior: float,
            valor_numerico: float,
            valor_texto: str,
            valor_booleano: bool,
    ) -> Resultado:
        if tipo_examen.es_texto or tipo_examen.es_imagen:
            if not valor_texto:
                raise HTTPException(status_code=400, detail="VALOR TEXTO REQUIRED")

            return Resultado(datetime.datetime.now(), self.id, valor_texto=valor_texto)
        elif tipo_examen.es_booleano:
            if not valor_booleano:
                raise HTTPException(status_code=400, detail="VALOR BOOLEANO REQUIRED")
            return Resultado(datetime.datetime.now(), self.id, valor_booleano=valor_booleano)

        else:
            if (not limite_superior) or (not limite_inferior) or (not valor_numerico):
                raise HTTPException(status_code=400, detail="NUMERIC DATA REQUIRED")
            return Resultado(datetime.datetime.now(), self.id, valor_numerico=valor_numerico,
                             limite_inferior=limite_inferior, limite_superior=limite_superior)
