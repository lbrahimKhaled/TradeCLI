import sqlite3
import json
import os
from uuid import UUID
from .models import TradeRecord

#here no need for the .env since this is the cache DB that saves prior results of prior executions
DB_PATH = os.path.join(os.path.dirname(__file__), "mock-db", "tradecli.db")

def get_element_by_id(id: UUID) -> TradeRecord:
    con = sqlite3.connect(DB_PATH)
    cur = con.cursor()
    rows = cur.execute(
        "SELECT variable_name, series FROM results WHERE script_id = ?", (str(id),)
    ).fetchall()
    con.close()
    variables = {name: json.loads(series) for name, series in rows}
    return TradeRecord(id=id, variables=variables)

def save_trade_record(record: TradeRecord) -> None:
    """
    this will save the given trade record to the database
    """
    # NB: there should be 2 savings the local save and the remote save to the company's DB
    pass
