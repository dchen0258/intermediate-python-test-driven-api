from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from database import DataBase

app = FastAPI()

app.db = DataBase()

# Bird data model
class Bird(BaseModel):
    name: str
    species: str

# GET endpoint to retrieve all birds
@app.get("/birds")
def get_all_birds():
    return app.db.all()

# GET endpoint to retrieve a specific bird by name
@app.get("/birds/{name}")
def get_bird(name: str):
    return app.db.get(name)

# POST endpoint to add a new bird
@app.post("/birds")
def add_bird(bird: Bird):
    app.db.put(bird.name.lower(), bird.dict())
    return app.db.get(bird.name.lower())

# DELETE endpoint to remove a bird by name
@app.delete("/birds/{name}")
def delete_bird(name: str):
    app.db.delete(name)
    return {"detail": "Bird deleted"}