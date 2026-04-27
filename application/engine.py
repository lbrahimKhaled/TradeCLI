""""
this file will be responsible for responsible for calling relevant transfomations / repo / functions  ...etc
"""

from tradecli_db.repo import get_element_by_id, save_trade_record
from tradecli_db.models import TradeRecord
def view_trade_record(id):
    """
    this will be responsible for calling the repo function to get the trade record by id and then print it in a nice format
    """
    record: TradeRecord = get_element_by_id(id)
    print(f"Trade Record for ID: {record.id}")
    for variable_name, series in record.variables.items():
        print(f"{variable_name}: {series}")


