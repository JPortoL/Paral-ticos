from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date
from sqlalchemy.orm import relationship

from .configuracion import Base


class ClinicoDB(Base):
    __tablename__ = "clinico"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    nombre = Column(String)
    apellido = Column(String)

class ExamenDB(Base):
    __tablename__ = "examen"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String)
    tipo = Column(String)
    fecha_creado = Column(Date)
    paciente = Column(String)
    estado = Column(String)
    clinico_id = Column(Integer, ForeignKey("clinico.id"))

    clinico = relationship("ClinicoDB", back_populates="examen")

# class Item(Base):
#     __tablename__ = "items"

#     id = Column(Integer, primary_key=True, index=True)
#     title = Column(String, index=True)
#     description = Column(String, index=True)
#     owner_id = Column(Integer, ForeignKey("users.id"))

#     owner = relationship("User", back_populates="items")