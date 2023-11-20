from fastapi import HTTPException
from DB.modelos import ClinicoDB, ExamenDB, ExamenTypeDB, ResultadoDB
from sqlalchemy.orm import Session
from clases.clinico import Clinico
from clases.examen import Examen
from clases.resultado import Resultado
from clases.tipoExamen import TipoExamen
from constantes.estadoExamen import EstadosExamen


class DatabaseCrud:

    @staticmethod
    def search_clinico(db: Session, id) -> Clinico:
        db_clinico = db.query(ClinicoDB).filter(ClinicoDB.id == id).first()
        if not db_clinico:
            raise HTTPException(status_code=404, detail="CLINICO NOT FOUND")
        return Clinico(db_clinico.nombre, db_clinico.apellido, db_clinico.email, db_clinico.id)

    @staticmethod
    def create_clinico(db: Session, clinico: Clinico) -> ClinicoDB:
        db_clinico = ClinicoDB(nombre=clinico.nombre, apellido=clinico.apellido, email=clinico.email)
        db.add(db_clinico)
        db.commit()
        db.refresh(db_clinico)
        return db_clinico

    @staticmethod
    def create_examen(db: Session, examen: Examen) -> ExamenDB:
        db_examen = ExamenDB(
            tipo_id=examen.tipo_id,
            fecha_creacion=examen.fecha_creacion,
            clinico_id=examen.clinico_id,
            paciente_id=examen.paciente_id,
            estado=examen.estado,
        )
        db.add(db_examen)
        db.commit()
        db.refresh(db_examen)
        return db_examen

    @staticmethod
    def search_examen(db: Session, id) -> Examen:
        examen = db.query(ExamenDB).filter(ExamenDB.id == id).first()
        if not examen:
            raise HTTPException(status_code=404, detail="EXAMEN NOT FOUND")
        return Examen(
            examen.tipo_id,
            examen.fecha_creacion,
            examen.paciente_id,
            examen.estado,
            examen.clinico_id,
            examen.id,
            examen.interpretacion,
            examen.fecha_interpretacion,
            examen.resultado_id,
        )

    @staticmethod
    def actualizar_examen_resultado_id(db: Session, id, resultado_id: int):
        db_examen = db.query(ExamenDB).filter(ExamenDB.id == id)
        db_examen.update({'resultado_id': resultado_id, 'estado': EstadosExamen.ESPERANDO_INTERPRETACION.value})
        db.commit()

    @staticmethod
    def actualizar_interpretacion_examen(db: Session, examen: Examen):
        db_examen = db.query(ExamenDB).filter(ExamenDB.id == examen.id)
        db_examen.update({'interpretacion': examen.interpretacion, 'estado': examen.estado,
                          "fecha_interpretacion": examen.fecha_interpretacion,
                          'clinico_interpreta_id': examen.clinico_interpreta_id})
        db.commit()

    @staticmethod
    def crear_resultado(db: Session, resultado: Resultado) -> ResultadoDB:
        db_resultado = ResultadoDB(
            fecha=resultado.fecha,
            clinico_id=resultado.clinico_id,
            valor_booleano=resultado.valor_booleano,
            valor_texto=resultado.valor_texto,
            valor_numerico=resultado.valor_numerico,
            limite_inferior=resultado.limite_inferior,
            limite_superior=resultado.limite_superior
        )
        db.add(db_resultado)
        db.commit()
        db.refresh(db_resultado)
        return db_resultado

    @staticmethod
    def search_resultado(db: Session, id) -> Resultado:
        resultado = db.query(ResultadoDB).filter(ResultadoDB.id == id).first()
        if not resultado:
            raise HTTPException(status_code=404, detail="RESULTADO NOT FOUND")
        return Resultado(
            resultado.fecha,
            resultado.clinico_id,
            resultado.valor_booleano,
            resultado.valor_texto,
            resultado.valor_numerico,
            resultado.limite_inferior,
            resultado.limite_superior,
            resultado.id,
        )

    @staticmethod
    def search_tipo_examen(db: Session, id) -> TipoExamen:
        te = db.query(ExamenTypeDB).filter(ExamenTypeDB.id == id).first()
        if not te:
            raise HTTPException(status_code=404, detail="EXAMEN TYPE NOT FOUND")
        return TipoExamen(te.id, te.nombre, te.es_numero, te.es_imagen, te.es_texto, te.es_booleano)
