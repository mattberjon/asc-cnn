import re


def write_config(section, option, data, config_obj, config_file):
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
    if config_obj.has_section(section):
        config_obj.set(section, option, str(data))
    else:
        config_obj.add_section(section)
        config_obj.set(section, option, str(data))

    config_obj.write(config_file)


def read_config(section, option, config_obj):
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
