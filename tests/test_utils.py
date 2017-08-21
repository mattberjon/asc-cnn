import pytest
from asc import utils


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
