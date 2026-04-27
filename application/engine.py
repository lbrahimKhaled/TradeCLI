""""
this file will be responsible for responsible for calling relevant transfomations / repo / functions  ...etc
"""

from uuid import UUID

from tradecli_db.repo import get_element_by_id, save_trade_record
from tradecli_db.models import TradeRecord
def view_trade_record(id: UUID, variables: tuple[str, ...] = ()) ->  tuple[dict[str, list[float]], set[str]]: # defualting variables to ()
    """
    this will be responsible for calling the repo function 
    to get the trade record by id and then print it in a nice format
    """
    record: TradeRecord = get_element_by_id(id)
    print(f"Trade Record for ID: {record.id}")
    variables_set = set(variables)
    return (record.variables, variables_set) if variables else (record.variables, set(record.variables.keys())) # if variables is empty we will return all the variables in the record


