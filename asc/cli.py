# -*- coding: utf-8 -*-

"""Console script for asc."""

import click
import configparser
import os
import sys
from shutil import copyfile

from . import __version__
from . import audio
from . import data
from . import utils

config_path = os.path.abspath(os.path.expanduser('~')) + '/.ascrc'
url_list_path = os.path.dirname(os.path.realpath(__name__)) \
        + '/samples/url_list.txt'


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
    utils.write_config(
            section,
            option,
            value,
            config_path)


@main.command()
def getdata():
    """Download dataset from the server.

    Download the dataset from the server and unzip the all in the default
    folder.
    """
    # Check the data folder. If the folder doesn't exist, we create it,
    # if it exist, then ask the user if we can override it before proceed
    # to do anything else and store the path in a config file.
    url_list = utils.read_config('path', 'url_list', config_path)
    tmp_path = utils.read_config('path', 'archive', config_path)
    data_path = utils.read_config('path', 'data', config_path)

    dest_path = os.path.abspath(data_path) + '/data'

    if os.path.isdir(dest_path):
        # python 3: needs to use input() instead of raw_input()
        user_input = raw_input(
                "The %s already exists, do you still want to proceed? [y/N]: "
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
    get_data.unzip_data(file_list, tmp_path, dest_path)


@main.command()
def setup():
    var_name = 'Root path of the project'
    default_value = '~/asc-data'
    ret_val = utils.read_user_input(var_name, default_value)
    root_path = os.path.abspath(os.path.expanduser(ret_val))

    # Setup the paths
    archive_path = root_path + '/archives'
    audio_path = root_path + '/audio'
    specs_path = root_path + '/spectrograms'
    
    # Create the directories
    if not os.path.isdir(root_path):
        os.makedirs(archive_path)
        os.makedirs(audio_path)
        os.makedirs(specs_path)

    # save the information in the config file
    section = 'path'
    utils.write_config(section, 'root', root_path, config_path)
    utils.write_config(section, 'archive', archive_path, config_path)
    utils.write_config(section, 'audio', archive_path, config_path)
    utils.write_config(section, 'spectrograms', specs_path, config_path)

    # Copy the URL file into the data folder
    url_list = root_path + '/url_list.txt'
    copyfile(url_list_path, url_list)
    utils.write_config(section, 'url_list', url_list, config_path)


if __name__ == "__main__":
    main()
