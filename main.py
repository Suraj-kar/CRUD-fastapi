from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="FastAPI CRUD with Separate Decorators")

# Pydantic schema
class Item(BaseModel):
    name: str
    description: str

# In-memory "DB"
items_db = {}

# CREATE
@app.post("/items/{id}")
def create_item(id: int, item: Item):
    if id in items_db:
        raise HTTPException(status_code=400, detail="Item already exists")
    items_db[id] = item
    return items_db[id]

# READ single item
@app.get("/items/{id}")
def read_item(id: int):
    if id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    return items_db[id]

# READ all items
@app.get("/items/")
def read_all_items():
    return items_db

# UPDATE
@app.put("/items/{id}")
def update_item(id: int, item: Item):
    if id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    items_db[id] = item
    return items_db[id]

# DELETE
@app.delete("/items/{id}")
def delete_item(id: int):
    if id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    del items_db[id]
    return {"message": "Item deleted"}
