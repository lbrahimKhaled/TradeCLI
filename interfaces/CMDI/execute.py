import click
import sys
from application.engine import execute_script

@click.command()
def execute():
    id =1000
    script = sys.stdin.read()
    context = execute_script(script)
    click.echo(f"Script successfully executed for ID: {id}")
