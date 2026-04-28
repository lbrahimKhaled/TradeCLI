import click
import sys
from application.engine import execute_script

@click.command()
def execute():
    script = sys.stdin.read()
    id = execute_script(script)
    click.echo(f"Script successfully executed: {id}")
