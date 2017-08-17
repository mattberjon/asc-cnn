from asc import asc
import pytest


def test_spectrogram():
    with pytest.raises(AttributeError):
        asc.spectrogram('string', 44100)

    with pytest.raises(AttributeError):
        asc.spectrogram([1, 2, 3], 'string')
