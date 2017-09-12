from asc import audio
import pytest


def test_spectrogram():
    with pytest.raises(AttributeError):
        audio.spectrogram('string', 44100)

    with pytest.raises(AttributeError):
        audio.spectrogram([1, 2, 3], 'string')
