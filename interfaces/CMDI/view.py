import click

@click.command()
@click.option("--id", prompt = True, help = "price entry and exit based on ID")
def view(id):
    click.echo(f"price entry exit result for ID: {id}")