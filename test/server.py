from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/hello")
def hello(your_name: str):
    return {"text": f"Hello {your_name}"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

class Produto(BaseModel):
    nome: str
    valor: float

@app.post("/produtos")
def produtos(produto: Produto):
    return {"mensagem": f"Produto ({produto.nome} - {produto.valor}) cadastrado com sucesso!"}