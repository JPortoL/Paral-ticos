import datetime


class Resultado:
    def __init__(
            self,
            fecha: datetime,
            clinico_id: int,
            valor_booleano: bool = None,
            valor_texto: str = None,
            valor_numerico: float = None,
            limite_inferior: float = None,
            limite_superior: float = None,
            id: int = None
    ):
        self.id = id
        self.fecha = fecha
        self.clinico_id = clinico_id
        self.limite_superior = limite_superior
        self.limite_inferior = limite_inferior
        self.valor_numerico = valor_numerico
        self.valor_texto = valor_texto
        self.valor_booleano = valor_booleano
