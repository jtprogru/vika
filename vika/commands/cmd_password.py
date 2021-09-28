import click
import secrets
import string


@click.command()
@click.option("-l", "--length", default=24, help="length of generated password")
def cli(length):
    """Generate password"""
    alphabet = string.ascii_letters + string.digits

    password = "".join(secrets.choice(alphabet) for _ in range(length))

    click.echo(click.style("Password: ", fg="green") + click.style(password, fg="red", bold=True))
