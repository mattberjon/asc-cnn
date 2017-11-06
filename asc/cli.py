# -*- coding: utf-8 -*-

"""Console script for asc."""

import click
import os
import sys
from shutil import copyfile

from . import __version__
from . import audio
from . import data
from . import utils
from config import App


config_path = App.config('CONFIG_PATH')
url_list_path = App.config('URL_PATH')


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
@click.option(
        '-D',
        '--debug',
        is_flag=True,
        help='Display each spectrograms per block')
def processing(frame_size, filename, mel_bands, frequency_max, debug):
    """ Set up the audio processing chain.
    """
    audio.process_audio(
            filename,
            frame_size,
            mel_bands,
            frequency_max,
            display=debug)


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
            value)


@main.command()
def getdata():
    """Download dataset from the server.

    Download the dataset from the server and unzip the all in the default
    folder.
    """
    # Check the data folder. If the folder doesn't exist, we create it,
    # if it exist, then ask the user if we can override it before proceed
    # to do anything else and store the path in a config file.
    try:
        url_list = utils.read_config('path', 'url_list')
        tmp_path = utils.read_config('path', 'archive')
        audio_path = utils.read_config('path', 'audio')

        # start download
        get_data = data.Data()
        file_list = get_data.file_to_list(url_list)
        get_data.download(file_list, tmp_path)

        # unzip the files
        get_data.unzip_data(file_list, tmp_path, tmp_path)

        # move the files into the audio folder
        get_data.move_files(file_list, audio_path, '*.wav')

    except ValueError:
        print('App not configured correclty, please run the following command: \
asc setup')
        sys.exit()


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
    utils.write_config(section, 'root', root_path)
    utils.write_config(section, 'archive', archive_path)
    utils.write_config(section, 'audio', archive_path)
    utils.write_config(section, 'spectrograms', specs_path)

    # Copy the URL file into the data folder
    url_list = root_path + '/url_list.txt'
    copyfile(url_list_path, url_list)
    utils.write_config(section, 'url_list', url_list)


if __name__ == "__main__":
    main()
