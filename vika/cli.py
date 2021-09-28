#!/usr/bin/env python3
# coding=utf-8
# Author: Michael (jtprogru) Savin
# WWW: https://jtprog.ru
# Email: mail@jtprog.ru
# Date: 2021-09-23

import click
import os


class ComplexCLI(click.MultiCommand):
    def list_commands(self, ctx):
        commands = []
        commands_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), "commands"))
        for filename in os.listdir(commands_folder):
            if filename.endswith(".py") and filename.startswith("cmd_"):
                commands.append(filename.replace("cmd_", "").replace(".py", ""))

        commands.sort()
        return commands

    def get_command(self, ctx, name):
        try:
            mod = __import__(f"vika.commands.cmd_{name}", None, None, ["cli"])
        except ImportError:
            return
        return mod.cli


@click.command(cls=ComplexCLI)
def cli():
    """Welcome to Vika! An all-in-one cli utility tool!"""
    pass
