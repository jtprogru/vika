#!/usr/bin/env python3
# coding=utf-8
# Author: Michael (jtprogru) Savin
# WWW: https://jtprog.ru
# Email: mail@jtprog.ru
# Date: 2021-06-29

import click

from .utils import gen, getpwd


@click.command()
@click.option('--count', default=3, help='number of generated promocodes')
@click.option('--lenght', default=5, help='lenght of generated promocodes')
def promocode(count, lenght):
    for _ in range(count):
        gen(lenght)


@click.command()
@click.option('--count', default=1, help='number of generated password')
@click.option('--length', default=24, help='length of generated password')
def password(count, length):
    for _ in range(count):
        getpwd(length)


@click.group()
def cli():
    pass


cli.add_command(promocode)
cli.add_command(password)


if __name__ == '__main__':
    cli()
