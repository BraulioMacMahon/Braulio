from pydantic import BaseModel


class Frase(BaseModel):
    id: int
    frase: str
    autor: str
    categoria: str

    class Config:
        orm_mode = True

class Categoria(BaseModel):
    id: int
    categoria: str

    class Config:
        orm_mode = True
