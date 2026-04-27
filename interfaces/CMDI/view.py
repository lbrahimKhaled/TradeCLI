import click
from application import engine
    
@click.command()
@click.option("--id", prompt = True, help = "price entry and exit based on ID")
def view(id):
    """
    this will send the request to the engine to get 
    the corresponding price entry and exit for the given ID and print the result
    """
    engine.view_trade_record(id)