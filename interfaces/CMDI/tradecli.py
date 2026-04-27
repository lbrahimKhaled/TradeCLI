import click
from . import view

@click.group()
def cli(ctx) -> None:
    click.echo("")

cli.add_command(view.view)
