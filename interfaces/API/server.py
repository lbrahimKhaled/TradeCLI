from fastapi import FastAPI, Query
from uuid import UUID
from typing import List
from application import engine
app = FastAPI()

@app.get("/view/{id}")
def view(id: UUID, items: List[str] | None = Query(None)): # meaning items can accept no arguments at all and will accept arguments if passed
    (record_variables, variables_set) = engine.view_trade_record(id) # means get everything from the DB all arguments and we will filter them here
    return {var: record_variables.get(var) for var in items} if items else record_variables