from fastapi import FastAPI
from app.database import init_db

app = FastAPI()

@app.on_event("startup")
def startup():
    init_db()

@app.get("/")
def root():
    return {"status": "Gestionale Allbrand attivo con Database"}
