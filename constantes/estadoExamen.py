from enum import Enum

# class syntax
class EstadosExamen(Enum):
    CREADO = "pendiente"
    ESPERANDO_INTERPRETACION = "esperando interpretacion"
    INTERPRETADO = "interpretado"
    FINALIZADO = "finalizado"