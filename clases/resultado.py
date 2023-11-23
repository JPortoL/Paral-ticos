import datetime


class Resultado:
    def __init__(
            self,
            fecha: datetime,
            clinico_id: int,
            valor_booleano: bool = None,
            valor_texto: str = None,
            valor_numerico: float = None,
            id: int = None,
            interpretacion: str = None,
            clinico_interpreta_id: int = None,

    ):
        self.id = id
        self.fecha = fecha
        self.clinico_id = clinico_id
        self.valor_numerico = valor_numerico
        self.valor_texto = valor_texto
        self.valor_booleano = valor_booleano
        self.interpretacion = interpretacion
        self.clinico_interpreta_id = clinico_interpreta_id
