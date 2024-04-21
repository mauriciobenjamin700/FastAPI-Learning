from fastapi import FastAPI
from typing import List, Optional
from pydantic import BaseModel
from uuid import uuid4

app = FastAPI()

class Animal(BaseModel):
    id: Optional[str]
    nome: str
    idade: int
    sexo: str
    cor: str

banco : List[Animal] = []

@app.get('/')
def home():
    return {"Hello": "World"}

@app.get('/animais')
def lista_animais():
    global banco
    return banco

@app.get('/animais/{animal_id}')
def obter_animal(animal_id: str):
    target = None
    for animal in banco:
        if animal.id == animal_id:
            target = animal
    
    return target


@app.post('/animais')
def criar_animal(animal: Animal):
    animal.id = str(uuid4())
    banco.append(animal)
    return True

@app.delete('/animais/{animal_id}')
def remover_animal(animal_id: str):
    position = -1
    msg = {"result": "Animal não encontrado"}
    global banco
    for index, animal in enumerate(banco):
        if animal.id == animal_id:
            position = index
            break
        
    if position != -1:
        msg['result'] = f"Animal {banco.pop(position).nome} removido com sucesso"