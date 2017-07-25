# -*- coding: utf-8 -*-

"""Console script for asc."""

import click
import sys

from . import __version__


def version_msg():
    """ Returns the program version, location and python version.
    """

    python_version = sys.version[:3]
    message = 'asc %(version)s (Python {})'
    return message.format(python_version)


@click.command(context_settings=dict(help_option_names=['-h', '--help']))
@click.version_option(
        __version__,
        '-V',
        '--version',
        message=version_msg(),
        help='Output the version of the application')
def main(args=None):
    """Console script for asc."""
    click.echo("Replace this message by putting your code into "
               "asc.cli.main")
    click.echo("See click documentation at http://click.pocoo.org/")


if __name__ == "__main__":
    main()
