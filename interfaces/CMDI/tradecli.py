import click
from . import view

@click.group(invoke_without_command = True)
@click.pass_context
def cli(ctx) -> None:
    #in case there is no subcommands invoked print the following message
    if ctx.invoked_subcommand is None:
        click.echo("usage: cli.py [-h] {execute,view} ... \n\n CLI tool \n\n positional arguments: \n {execute,view} \n execute Read entire stdin as input script \n view View items by ID \n\n options:\n-h, --help show this help message and exit")

cli.add_command(view.view)
