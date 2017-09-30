import pytest
from asc import audio
from librosa.util.exceptions import ParameterError
import numpy as np
import os


def test_extract_audio_data():
    data_path = os.path.dirname(os.path.realpath(__name__))
    audio_file = data_path + '/audio_data/sine_44100_2ch.wav'

    with pytest.raises(RuntimeError):
        audio.extract_audio_data('something_wrong')

    chan_nb, samplerate = audio.extract_audio_data(audio_file)
    assert chan_nb == 1
    assert samplerate == 44100


def test_static_spectrogram():
    with pytest.raises(ParameterError):
        audio.static_spectrogram(1)

    with pytest.raises(ParameterError):
        audio.static_spectrogram(np.array([1, 2, 3]), x_axis='something')

    with pytest.raises(ParameterError):
        audio.static_spectrogram(np.array([1, 2, 3]), y_axis='something')

    with pytest.raises(ValueError):
        audio.static_spectrogram(np.array([1, 2, 3]), mel_bands='string')

    with pytest.raises(TypeError):
        audio.static_spectrogram(np.array([1, 2, 3]), fmax='string')
