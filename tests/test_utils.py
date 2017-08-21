import pytest
from asc import utils


def test_read_config(config):
    with pytest.raises(ValueError):
        utils.read_config('something', 'nonexisting', config)

    config.add_section('audio')
    config.set('audio', 'samplerate', '44100')
    assert utils.read_config('audio', 'samplerate', config) == '44100'


def test_conf_param_extract():
    with pytest.raises(TypeError):
        utils.conf_param_extract(1000)

    section, option = utils.conf_param_extract('audio.samplerate')
    assert section == 'audio'
    assert option == 'samplerate'


def test_ms2smp():
    with pytest.raises(TypeError):
        utils.ms2smp('string', 44100)

    with pytest.raises(TypeError):
        utils.ms2smp(1000, 'string')

    assert utils.ms2smp(1000, 44100) == 44100
