from fastapi import Depends, FastAPI
from DB.configuracion import SessionLocal
from clases.clinico import Clinico
from DB.crud import crud_create_clinico, crud_search_clinico, crud_create_examen
from sqlalchemy.orm import Session

app = FastAPI(title="paraliticos")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/crear_examen")
def crear_examen(id_clinico: int, nombre: str, tipo: str, id_paciente: int, db: Session = Depends(get_db)):
    clinico = crud_search_clinico(db, id_clinico)
    examen = clinico.crear_examen(nombre, tipo, id_paciente)
    examen_creado = crud_create_examen(db, examen)
    return {"mensaje": "Examen creado", "examen": examen_creado}


@app.post("/crear_clinino")
def crear_clinino(nombre: str, apellido: str, email: str, db: Session = Depends(get_db)):
    clinico = Clinico(nombre, apellido, email)
    clinico_creado = crud_create_clinico(db, clinico)
    return {"mensaje": "Clinino creado", "clinico": clinico_creado}
