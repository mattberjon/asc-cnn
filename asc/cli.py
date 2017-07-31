# -*- coding: utf-8 -*-

"""Console script for asc."""

import click
import configparser
import os
import sys

from . import __version__
from . import data

config = configparser.ConfigParser()


def version_msg():
    """ Returns the program version, location and python version.
    """

    python_version = sys.version[:3]
    message = 'asc %(version)s (Python {})'
    return message.format(python_version)


@click.group(context_settings=dict(help_option_names=['-h', '--help']))
@click.version_option(
        __version__,
        '-V',
        '--version',
        message=version_msg(),
        help='Output the version of the application')
@click.pass_context
def main(ctx):
    """Console script for Acoustic Scene Classification (ASC).

    Need to set a better docstring.
    """
    pass


@main.command()
@click.option(
        '-u',
        '--url-file',
        type=click.Path(),
        help='Path to the file containing the URLs to download')
@click.option(
        '-t',
        '--tmp-dir',
        type=click.Path(),
        default='/tmp',
        help='Path to the temporary download folder. [default=/tmp]')
@click.option(
        '-d',
        '--dest-dir',
        type=click.Path(),
        default=os.path.expanduser('~'),
        help='Path to the data folder. [default=$HOME]')
def getdata(url_file, tmp_dir, dest_dir):
    """Download dataset from the server.

    Download the dataset from the server and unzip the all in the default
    folder.
    """
    # Check the data folder. If the folder doesn't exist, we create it,
    # if it exist, then ask the user if we can override it before proceed
    # to do anything else and store the path in a config file.
    dest_path = dest_dir + '/data'

    if os.path.isdir(dest_path):
        # python 3: needs to use input() instead of raw_input()
        user_input = raw_input(
                "The %s already exists, do you still want to proceed? [y/N]"
                % dest_path)
        if user_input == 'y':
            click.echo("Ok! let's continue to the next step")
        else:
            click.echo("Ok, bye!")
            sys.exit()
    else:
        click.echo('path doesnt exist')
        # Create the folder
        os.makedirs(dest_path)
        click.echo("Folder created!")
        # store the path into a config file for later use

    if url_file is None:
        click.echo('You must specify a file containing the urls to download')
        sys.exit()
    else:
        pass

    # start download
    get_data = data.Data()
    file_list = get_data.file_to_list(url_file)
    get_data.download(file_list, tmp_dir)

    # unzip the files
    get_data.unzip(file_list, tmp_dir, dest_dir)


if __name__ == "__main__":
    main()
