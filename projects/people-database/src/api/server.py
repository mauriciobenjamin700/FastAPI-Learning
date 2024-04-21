from fastapi import FastAPI

app = FastAPI()


@app.get("/database")
def get_database(): ...
@app.get("/item/{item_name}")
def search_item(item_name): ...
@app.delete("/delete/{item_name}")
def delete_item(item_name): ...


@app.post("/add/{register}")
def add_item(
    name, description, gender, country, occupation, birth, death, cause_death, age_death
): ...
