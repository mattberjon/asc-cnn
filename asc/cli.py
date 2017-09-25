# -*- coding: utf-8 -*-

"""Console script for asc."""

import click
import configparser
import os
import sys

from . import __version__
#  from . import audio
from . import data
from . import utils
from . import audio

config_path = os.path.expanduser('~') + '/.ascrc'


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
        '-f',
        '--filename')
@click.option(
        '-fs',
        '--frame-size',
        type=int,
        default=1,
        help='Frame size in samples. 1 frame=512 samples [default=1]')
@click.option(
        '-m',
        '--mel-bands',
        type=int,
        default=128,
        help='Number of mel bands to compute the dynamic spectrogram.\
                [default=128]')
@click.option(
        '-fm',
        '--frequency-max',
        type=int,
        default=22050,
        help='Frequency max to apply to the mel band in Hertz.\
                [default=22050]')
def processing(frame_size, filename, mel_bands, frequency_max):
    """ Set up the audio processing chain.
    """
    audio.process_audio(
            filename,
            frame_size,
            mel_bands,
            frequency_max,
            display=True)


@main.command()
@click.argument('parameter')
@click.argument('value')
def config(parameter, value):
    """ Configure the project.

    Save the configuration into the configuration file [default=~/.ascrc]
    See the documentation for the available list of parameters and values.
    """
    # Separation the section from the option
    section, option = utils.conf_param_extract(parameter)
    config = configparser.ConfigParser()
    config.read(config_path)
    config_file = open(config_path, 'w')
    utils.write_config(
            section,
            option,
            value,
            config,
            config_file)


#  @click.option(
#          '-u',
#          '--url-file',
#          type=click.Path(),
#          help='Path to the file containing the URLs to download')
#  @click.option(
#          '-t',
#          '--tmp-dir',
#          type=click.Path(),
#          default='/tmp',
#          help='Path to the temporary download folder. [default=/tmp]')
#  @click.option(
#          '-d',
#          '--dest-dir',
#          type=click.Path(),
#          default=os.path.expanduser('~'),
#          help='Path to the data folder. [default=$HOME]')
@main.command()
def getdata():
    """Download dataset from the server.

    Download the dataset from the server and unzip the all in the default
    folder.
    """
    # Check the data folder. If the folder doesn't exist, we create it,
    # if it exist, then ask the user if we can override it before proceed
    # to do anything else and store the path in a config file.
    config = configparser.ConfigParser()
    config.read(config_path)

    url_list = utils.read_config('path', 'url_list', config)
    tmp_path = utils.read_config('path', 'tmp', config)
    data_path = utils.read_config('path', 'data', config)

    dest_path = os.path.abspath(data_path) + '/data'

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

    # start download
    get_data = data.Data()
    file_list = get_data.file_to_list(url_list)
    get_data.download(file_list, tmp_path)

    # unzip the files
    get_data.unzip(file_list, tmp_path, dest_path)


if __name__ == "__main__":
    main()
