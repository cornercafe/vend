from fastapi import FastAPI
from datetime import datetime

from models import NewteaModel
app = FastAPI()

merchantid= '123456'

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/tea/new")
def newtea(tea:NewteaModel):
    # Calculate Date

    # Store request in db

    # Check Status and Levels

    # Call paytm api

    # Create new task to poll txn resul api.

    # return qr response

    return tea