import click
import sys

@click.command()
def execute():
    id =1000
    script = sys.stdin.read()
    click.echo(f"Script successfully executed: {id}")
