from os.path import abspath, dirname
import sys

sys.path.insert(0, dirname(dirname(abspath(__file__))))

from fastapi import FastAPI
from database import *

app = FastAPI()
db = DataBase()


@app.get("/database")
def get_database():
    global db
    return {"database": db.execute(get_all_registers())}

@app.get("/item/{item_name}")
def search_item(item_name): ...
@app.delete("/delete/{item_name}")
def delete_item(item_name): ...


@app.post("/add/{register}")
def add_item(
    name, 
    description, 
    gender, 
    country, 
    occupation, 
    birth, 
    death, 
    cause_death, 
    age_death
): 
    global db
    db.execute(
                    add_register(), 
                    (
                        name, 
                        description, 
                        gender, 
                        country, 
                        occupation, 
                        birth, 
                        death, 
                        cause_death, 
                        age_death
                    )
                ) 
    return {"mensage": "Cadastro realizado com sucesso"}