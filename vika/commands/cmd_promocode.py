import click
import secrets
import string


def gen(lenght):

    alphabet = string.ascii_uppercase + string.digits
    promo = ""

    for _ in range(lenght):
        promo += "".join(secrets.choice(alphabet))
    print(promo)


@click.command()
@click.option("--count", default=3, help="number of generated promocodes")
@click.option("--lenght", default=5, help="lenght of generated promocodes")
def cli(count, lenght):
    """Generate promocode"""
    for _ in range(count):
        gen(lenght)
