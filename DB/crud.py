from fastapi import HTTPException
from DB.modelos import ClinicoDB, ExamenDB
from sqlalchemy.orm import Session
from clases.clinico import Clinico
from clases.examen import Examen


def crud_search_clinico(db: Session, id: int) -> Clinico:
    db_clinico = db.query(ClinicoDB).filter(ClinicoDB.id == id).first()
    if not db_clinico:
        raise HTTPException(status_code=404, detail="CLINICO NOT FOUND")
    return Clinico(db_clinico.nombre, db_clinico.apellido, db_clinico.email, db_clinico.id)


def crud_create_clinico(db: Session, clinico: Clinico):
    db_clinico = ClinicoDB(nombre=clinico.nombre, apellido=clinico.apellido, email=clinico.email)
    db.add(db_clinico)
    db.commit()
    db.refresh(db_clinico)
    return db_clinico


def crud_create_examen(db: Session, examen: Examen):
    db_examen = ExamenDB(
        nombre=examen.nombre,
        tipo=examen.tipo,
        fecha_creacion=examen.fecha_creacion,
        clinico_id=examen.clinico_id,
        paciente=examen.paciente,
        estado=examen.estado,
    )
    db.add(db_examen)
    db.commit()
    db.refresh(db_examen)
    return db_examen
