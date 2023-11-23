from fastapi import Depends, FastAPI, HTTPException
from DB.configuracion import SessionLocal
from clases.clinico import Clinico
from DB.crud import DatabaseCrud
from sqlalchemy.orm import Session

from constantes.estadoExamen import EstadosExamen

app = FastAPI(title="Paraclinicos")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/crear_examen", tags=["Examen"])
def crear_examen(id_clinico: int, tipo_examen_id: int, id_paciente: int, db: Session = Depends(get_db)):
    clinico = DatabaseCrud.search_clinico(db, id_clinico)
    tipo_examen = DatabaseCrud.search_tipo_examen(db, tipo_examen_id)
    examen = clinico.crear_examen(tipo_examen, id_paciente)
    examen_creado = DatabaseCrud.create_examen(db, examen)
    return {"mensaje": "Examen creado", "examen": examen_creado}


@app.post("/crear_resultado", tags=["Examen"])
def crear_resultado(
        id_clinico: int,
        id_examen: int,
        valor_numerico: float = None,
        valor_texto: str = None,
        valor_booleano: bool = None,
        db: Session = Depends(get_db)
):
    clinico = DatabaseCrud.search_clinico(db, id_clinico)
    examen = DatabaseCrud.search_examen(db, id_examen)
    if examen.estado != EstadosExamen.CREADO.value:
        raise HTTPException(status_code=400, detail="EL EXAMEN YA TIENE RESULTADO")
    tipo_examen = DatabaseCrud.search_tipo_examen(db, examen.tipo_id)
    resultado = clinico.registrar_resultado(tipo_examen, valor_numerico, valor_texto, valor_booleano)
    resultado_creado = DatabaseCrud.crear_resultado(db, resultado)
    examen.registrar_examen(resultado_creado.id)
    DatabaseCrud.actualizar_examen_resultado_id(db, examen.id, resultado_creado.id)
    resultado.id = resultado_creado.id
    return {"mensaje": "Resultado Registrado", "examen": examen, "resultado": resultado}


@app.patch("/interpretar_examen", tags=["Examen"])
def interpretar_examen(id_clinico: int, id_examen: int, interpretacion: str, db: Session = Depends(get_db)):
    clinico = DatabaseCrud.search_clinico(db, id_clinico)
    examen = DatabaseCrud.search_examen(db, id_examen)
    resultado = DatabaseCrud.search_resultado(db, examen.resultado_id)
    if examen.estado == EstadosExamen.CREADO.value:
        raise HTTPException(status_code=400, detail="EL EXAMEN NO TIENE RESULTADO")
    if examen.estado == EstadosExamen.FINALIZADO.value:
        raise HTTPException(status_code=400, detail="EL EXAMEN YA ESTÁ INTERPRETADO")
    clinico.interpretar_examen(examen, resultado, interpretacion)
    DatabaseCrud.actualizar_interpretacion_examen(db, examen)
    DatabaseCrud.actualizar_interpretacion_resultado(db, resultado)
    return {"mensaje": "Examen interpretado", "examen": examen, "resultado": resultado}


@app.get("/buscar-examen", tags=["Examen"])
def buscar_examen_completo(id_examen, db: Session = Depends(get_db)):
    examen = DatabaseCrud.search_examen(db, id_examen)
    tipo_examen = DatabaseCrud.search_tipo_examen(db, examen.tipo_id)
    examen.tipo = {'id': tipo_examen.id, 'name': tipo_examen.nombre}
    response_resultado = None
    if examen.resultado_id:
        resultado = DatabaseCrud.search_resultado(db, examen.resultado_id)
        if tipo_examen.es_imagen or tipo_examen.es_texto:
            response_resultado = {'valor': resultado.valor_texto}
        elif tipo_examen.es_booleano:
            response_resultado = {'valor': resultado.valor_booleano}
        else:
            response_resultado = {'valor': resultado.valor_numerico, 'limite_superior': tipo_examen.limite_superior,
                                  'limite_inferior': tipo_examen.limite_inferior}
    return {"examen": examen, "resultado": response_resultado}


@app.post("/crear_clinico", tags=["Clinico"])
def crear_clinino(nombre: str, apellido: str, email: str, db: Session = Depends(get_db)):
    clinico = Clinico(nombre, apellido, email)
    clinico_creado = DatabaseCrud.create_clinico(db, clinico)
    return {"mensaje": "Clinino creado", "clinico": clinico_creado}
