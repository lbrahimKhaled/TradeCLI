import sqlite3
import json
import os
import csv
from uuid import UUID, uuid4
from .models import TradeRecord

#here no need for the .env since this is the cache DB that saves prior results of prior executions
DB_PATH = os.path.join(os.path.dirname(__file__), "mock-db", "tradecli.db")
#putting them like that is extremely useful since if the path changes we don't need to modify every line where these are mentioned
#helping and facilitating maintainability
DATA_PATH = os.path.join(os.path.dirname(__file__), "mock-db", "fetch_transformation_data.csv")


def get_element_by_id(id: UUID) -> TradeRecord:
    con = sqlite3.connect(DB_PATH)
    cur = con.cursor()
    rows = cur.execute(
        "SELECT variable_name, series FROM results WHERE script_id = ?", (str(id),)
    ).fetchall()
    con.close()
    variables = {name: json.loads(series) for name, series in rows}
    return TradeRecord(id=id, variables=variables)

def save_trade_record(variables: dict[str, list[float]]) -> UUID:
    """
    given the variable names and the corresponding series
    we will save them to the db and generate a unique ID for the whole variables to group them
    return : the unique ID previously generated
    """
    id = uuid4()
    record = TradeRecord(id=id, variables=variables)
    con = sqlite3.connect(DB_PATH)
    cur = con.cursor()
    cur.executemany(
        "INSERT INTO results (script_id, variable_name, series) VALUES (?, ?, ?)",
        [(str(record.id), name, json.dumps(series)) for name, series in record.variables.items()]
    )
    con.commit()
    con.close()
    return id



def get_datasource_by_name(datasource: str) -> list[float]:
    """
    this will get the datasource by name from the CSV file and return the corresponding data as a list of floats
    """
    with open(DATA_PATH, encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["label"] == datasource:
                return [float(x) for x in row["series"].split(",")]
    return []