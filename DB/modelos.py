from sqlalchemy import Column, ForeignKey, Integer, String, Date

from .configuracion import Base


class ClinicoDB(Base):
    __tablename__ = "clinico"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    nombre = Column(String)
    apellido = Column(String)


class ExamenDB(Base):
    __tablename__ = "examenes"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String)
    tipo = Column(String)
    fecha_creacion = Column(Date)
    fecha_interpretacion = Column(Date, nullable=True)
    resultado_id = Column(Integer, nullable=True)
    clinico_id = Column(Integer, ForeignKey("clinico.id"))
    interpretacion = Column(String, nullable=True)
    paciente = Column(String)
    estado = Column(String, index=True)
