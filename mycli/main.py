import click
import cowsay

@click.group()
def cli():
    pass

@cli.command()  # @cli, not @click!
@click.argument('input')
def hello(input):
    click.echo(cowsay.get_output_string('tux', f'Hello {input}'))
