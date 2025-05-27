# Smurf API - Testprojekt
# AUTHOR Sven Schrodt<sven.schrodt@schrodt.club
# SINCE 2025-05-19
# LINK https://github.com/nevsglueckauf/smurf_api

import pandas
from typing import Union
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.get("/impressum/")
def read_imp():
    return {"author": "Sven Schrodt", "link_gh": "https://github.com/nevsglueckauf/smurf_api"}
