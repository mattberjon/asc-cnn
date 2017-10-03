import click
import configparser
import os
import re
from config import App

config_path = App.config('CONFIG_PATH')


def write_config(section, option, data):
    """ Write/Update the configuration file

    Write or update the configuration file according to the section or
    option provided.

    Args:
        section (str): Name of the section
        option (str): Name of the option
        data (str): data related to the option to store
        config_obj (str): instance of the configuration object)
        config_file (str): instance of the configuration file where to save
                            the data

    Returns:
        None

    Todo:
        Need to cast the object to string before saving the data.
    """
    config_obj = configparser.ConfigParser()
    config_obj.read(config_path)
    config_file = open(config_path, 'w')
    if config_obj.has_section(section):
        config_obj.set(section, option, str(data))
    else:
        config_obj.add_section(section)
        config_obj.set(section, option, str(data))

    config_obj.write(config_file)
    config_file.close()


def read_config(section, option):
    """ Look for a given option in a config file.

    If exists, return the value in a config file according to the section
    and option.

    Args:
        section (str):  section related to the option looked for.
        option (str):   option related to the value looked for.
        config_obj (obj):   configparser object.

    Returns:
        value given for a specific tuple section/option.

    Todo:
        - Be able to cast the data into the right type.
    """
    config_obj = configparser.ConfigParser()
    config_obj.read(config_path)

    if config_obj.has_option(section, option):
        return config_obj.get(section, option)
    else:
        raise ValueError(
                "Impossible to find %s.%s in the configuration file"
                % (section, option))


def conf_param_extract(parameter):
    """ Extract the section and option given the parameter.

    Extract the section and option given the parameter that is in the
    specific format section.option

    Args:
        parameter (str): parameter with the format 'section.option'

    Returns:
        The section and option
    """
    data = re.split('\.', parameter)
    section = data[0]
    option = data[1]
    return section, option


def ms2smp(ms, sample_rate):
    """Milliseconds to samples converter.

    Simple converter in order to compute the number of samples for a given
    time frame in milliseconds and the sampling rate.

    Args:

        ms (int):           Number of milliseconds.
        sample_rate (int):  Sampling rate in Hertz.

    Returns:
        Return the number of sample (forced as an int).

    """
    # The factor of 0.001 is to convert the value in milliseconds into seconds.
    # This is done because a sample rate is given in seconds.
    return int(ms * sample_rate * 0.001)


def read_user_input(var_name, default_value):
    """ Prompt the user for the given variable and return the entered value
    or the given default.

    Args:
        var_name (str): Variable of the context to query the user
        default_value (str): Value that will be returned if no input happens

    Return
        The user input or the default value

    """
    return click.prompt(var_name, default=default_value)


def read_user_yes_no(question, default_value):
    """ Prompt the user to reply with 'yes' or 'no' (or equivalent).

    Args:
        question (str): Question to the user
        default_value (bool): Value that will be returned if no input happens

    Returns:
        The user input or the default value

    Note:
        Possible choices are 'true', '1', 'yes', 'y' or 'false', '0', 'no', 'n'

    """
    return click.prompt(
            question,
            default=default_value,
            type=clik.BOOL)


def create_filename(save_path, extension, *args):
    """ Create a filename based on any pattern.

    Args:
        save_path (str): Path where the file will be saved
        extension (str): the extension of the file (without the '.')
        args: any other argument needed to create the filename pattern.

    Returns:
        A string containing the path and its file name.

    Note:
        All the arguments passed to the pattern are casted as strings in order
        to avoid any issues.

    Todo:
        Check that the extension doesn't contain any '.' and remove it if
        necessary.
    """

    fname = []
    for count, argument in enumerate(args):
        fname.append(str(argument) + '_')

    total_path = os.path.abspath(save_path) + '/' + ''.join(fname) + '.' + extension
    return total_path
