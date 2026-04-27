import click
from application import engine
    
@click.command()
@click.option("--id", prompt = True, help = "price entry and exit based on ID")
@click.argument("variables", nargs=-1) # meaning variables will be as a tuple and doesn't matter the number of args passed                                                            
def view(id, variables):
    """
    this will send the request to the engine to get 
    the corresponding price entry and exit for the given ID and print the result
    """
    engine.view_trade_record(id, variables)