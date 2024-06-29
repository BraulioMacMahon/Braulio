from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import func, select

from . import models


def pegarFraseAleatoria(db: Session):
    return db.query(models.Frase).order_by(func.random()).first()


def pegarFraseAleatoriaPorCategoria(db: Session, categoria: str):
    return db.query(models.Frase).filter(models.Frase.categoria == categoria).order_by(func.random()).first()

def pegarTodasFrases(db: Session):
    return db.query(models.Frase).all()

def pegarTodasCategorias(db: Session):
    return db.query(models.Categoria).all()

   