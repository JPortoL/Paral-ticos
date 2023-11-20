from sqlalchemy import Column, ForeignKey, Integer, String, Date, Boolean, Double

from .configuracion import Base


class ClinicoDB(Base):
    __tablename__ = "clinico"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    nombre = Column(String)
    apellido = Column(String)


class ExamenTypeDB(Base):
    __tablename__ = "tipo_examen"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nombre = Column(String)
    es_numero = Column(Boolean, default=False)
    es_imagen = Column(Boolean, default=False)
    es_texto = Column(Boolean, default=False)
    es_booleano = Column(Boolean, default=False)


class ExamenDB(Base):
    __tablename__ = "examenes"

    id = Column(Integer, primary_key=True, index=True)
    tipo_id = Column(Integer, ForeignKey("tipo_examen.id"))
    fecha_creacion = Column(Date)
    fecha_interpretacion = Column(Date, nullable=True)
    resultado_id = Column(Integer, ForeignKey("resultados.id"), nullable=True)
    clinico_interpreta_id = Column(Integer, ForeignKey("clinico.id"), nullable=True)
    clinico_id = Column(Integer, ForeignKey("clinico.id"))
    interpretacion = Column(String, nullable=True)
    paciente_id = Column(Integer)
    estado = Column(String, index=True)


class ResultadoDB(Base):
    __tablename__ = "resultados"

    id = Column(Integer, primary_key=True, index=True)
    fecha = Column(Date)
    clinico_id = Column(Integer, ForeignKey("clinico.id"))
    limite_superior = Column(Double, nullable=True)
    limite_inferior = Column(Double, nullable=True)
    valor_numerico = Column(Double, nullable=True)
    valor_texto = Column(String, nullable=True)
    valor_booleano = Column(Boolean, nullable=True)
