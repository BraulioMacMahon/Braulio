from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, TIMESTAMP, Time,func

from .database import Base


class Frase(Base):
    __tablename__ = "frases"

    id = Column(Integer, primary_key = True)
    frase = Column(String)
    autor = Column(String)
    categoria = Column(String)

class Categoria(Base):
    __tablename__  = "categorias"

    id = Column(Integer, primary_key=True)
    categoria = Column(String)


