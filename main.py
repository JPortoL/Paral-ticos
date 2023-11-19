from fastapi import Depends, FastAPI
from DB.configuracion import SessionLocal
from clases.examen import Examen
from clases.clinico import Clinico
from DB.crud import crud_create_clinico
from sqlalchemy.orm import Session

app = FastAPI(title="paraliticos")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/crear_examen")
def crear_examen():
    return {"mensaje": "Examen creado"}

@app.post("/crear_clinino")
def crear_clinino(nombre: str , apellido: str, email: str, db: Session = Depends(get_db)):
    clinico = Clinico(nombre, apellido, email)
    clinico_creado = crud_create_clinico(db, clinico)
    return {"mensaje": "Clinino creado", "clinico": clinico_creado}