from enum import Enum

# class syntax
class EstadosExamen(Enum):
    CREADO = "creado"
    ESPERANDO_INTERPRETACION = "esperando interpretacion"
    INTERPRETADO = "interpretado"
    FINALIZADO = "finalizado"