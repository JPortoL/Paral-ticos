from DB.modelos import ClinicoDB
from sqlalchemy.orm import Session
from clases.clinico import Clinico


def crud_create_clinico(db: Session, clinico: Clinico):
    db_clinico = ClinicoDB(nombre=clinico.nombre, apellido=clinico.apellido, email=clinico.email)
    db.add(db_clinico)
    db.commit()
    db.refresh(db_clinico)
    return db_clinico