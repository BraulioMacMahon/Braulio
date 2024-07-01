from typing import Union
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/api/categorias/", response_model=list[schemas.Categoria], summary="Retorna categorias disponíveis")
def categorias(db: Session = Depends(get_db)):
    categorias = crud.pegarTodasCategorias(db)
    return categorias

@app.get("/api/frase/aleatoria/categoria={categoria}", response_model=schemas.Frase, summary="Retorna uma frase aleatoria na categoria especificada")
def fraseAleatoriaPorCategoria(categoria: str, db: Session = Depends(get_db)):
    frase = crud.pegarFraseAleatoriaPorCategoria(db, categoria)
    return frase

@app.get("/api/frase/aleatoria/", response_model=schemas.Frase, summary="Retorna uma fase aleatoria")   
def fraseAleatoria(db: Session = Depends(get_db)):
    frases = crud.pegarFraseAleatoria(db)
    return frases

@app.get("/api/frase/", response_model=list[schemas.Frase], summary="Retorna todas as frases existentes")   
def todasFrases(db: Session = Depends(get_db)):
    frases = crud.pegarTodasFrases(db)
    return frases