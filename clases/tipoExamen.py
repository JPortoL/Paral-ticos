class TipoExamen:
    def __init__(
            self,
            id: int,
            nombre: str,
            es_numero: bool,
            es_imagen: bool,
            es_texto: bool,
            es_booleano: bool
    ):
        self.id = id
        self.nombre = nombre
        self.es_numero = es_numero
        self.es_imagen = es_imagen
        self.es_texto = es_texto
        self.es_booleano = es_booleano
