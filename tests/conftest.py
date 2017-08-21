from click.testing import CliRunner
import configparser
import pytest
import os


@pytest.fixture(scope='function')
def runner(request):
    return CliRunner()


@pytest.fixture(scope='function')
def config():
    """ Returns an instance of the config. """
    config = configparser.ConfigParser()
    return config
