import pytest
from asc import audio
from librosa.util.exceptions import ParameterError
import numpy as np


def test_static_spectrogram():
    with pytest.raises(ParameterError):
        audio.static_spectrogram(1)

    with pytest.raises(ValueError):
        audio.static_spectrogram(np.array([1, 2, 3]), mel_bands='string')

    with pytest.raises(TypeError):
        audio.static_spectrogram(np.array([1, 2, 3]), fmax='string')
