""""
this file will be responsible for responsible for calling relevant transfomations / repo / functions  ...etc
"""

from uuid import UUID

from tradecli_db.repo import get_element_by_id, save_trade_record, get_datasource_by_name
from tradecli_db.models import TradeRecord
from application.translater import parse_script
from application.transformations.sma import simple_moving_average
from application.transformations.ema import exponential_moving_average
from application.transformations.roc import rate_of_change
from application.transformations.cross_above import cross_above
from application.transformations.constant_series import constant_series
from application.transformations.portfolio_simulation import portfolio_simulation

def fetch_record(datasource: str) -> list[float] :
    """
    responsible for calling the repo for 
    """
    data = get_datasource_by_name(datasource)
    return data


def view_trade_record(id: UUID, variables: tuple[str, ...] = ()) ->  tuple[dict[str, list[float]], set[str]]: # defualting variables to ()
    """
    this will be responsible for calling the repo function 
    to get the trade record by id and then print it in a nice format
    """
    record: TradeRecord = get_element_by_id(id)
    print(f"Trade Record for ID: {record.id}")
    variables_set = set(variables)
    return (record.variables, variables_set) if variables else (record.variables, set(record.variables.keys())) # if variables is empty we will return all the variables in the record

def execute_script(script: str) -> dict[str, list[float]]:
    statements = parse_script(script)
    context: dict[str, list[float]] = {}

    for variable, transformation, config, series_refs in statements:
        series_inputs = [context[ref] for ref in series_refs]

        match transformation:
            case "Fetch":
                context[variable] = fetch_record(config[0])
            case "SimpleMovingAverage":
                context[variable] = simple_moving_average(int(config[0]), series_inputs[0])
            case "ExponentialMovingAverage":
                context[variable] = exponential_moving_average(float(config[0]), series_inputs[0])
            case "RateOfChange":
                context[variable] = rate_of_change(int(config[0]), series_inputs[0])
            case "CrossAbove":
                context[variable] = cross_above(series_inputs[0], series_inputs[1])
            case "ConstantSeries":
                context[variable] = constant_series(float(config[0]), series_inputs[0])
            case "PortfolioSimulation":
                context[variable] = portfolio_simulation(float(config[0]), series_inputs[0], series_inputs[1], series_inputs[2])
            # here later might go some error handling
    return context
    