from DB.modelos import ClinicoDB, ExamenDB
from sqlalchemy.orm import Session
from clases.clinico import Clinico
from clases.examen import Examen


def crud_create_clinico(db: Session, clinico: Clinico):
    db_clinico = ClinicoDB(nombre=clinico.nombre, apellido=clinico.apellido, email=clinico.email)
    db.add(db_clinico)
    db.commit()
    db.refresh(db_clinico)
    return db_clinico

def crud_create_examen(db: Session, examen: Examen):
    db_examen = ExamenDB(nombre=examen.nombre, tipo=examen.tipo, fecha=examen.fecha, paciente=examen.paciente, estado=examen.estado)
    db.add(db_examen)
    db.commit()
    db.refresh(db_examen)
    return db_examen