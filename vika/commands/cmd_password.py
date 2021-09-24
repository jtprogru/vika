import click

from vika.utils.utils import getpwd


@click.command()
@click.option("-c", "--count", default=1, help="number of generated password")
@click.option("-l", "--length", default=24, help="length of generated password")
def cli(count, length):
    """Generate password"""
    for _ in range(count):
        getpwd(length)
