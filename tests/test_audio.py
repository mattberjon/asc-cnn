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
    filename = 'something'

    with pytest.raises(ParameterError):
        audio.static_spectrogram(1, filename)

    with pytest.raises(ParameterError):
        audio.static_spectrogram(
                np.array([1, 2, 3]),
                filename,
                x_axis='something')

    with pytest.raises(ParameterError):
        audio.static_spectrogram(
                np.array([1, 2, 3]),
                filename,
                y_axis='something')

    with pytest.raises(ValueError):
        audio.static_spectrogram(
                np.array([1, 2, 3]),
                filename,
                mel_bands='string')

    with pytest.raises(TypeError):
        audio.static_spectrogram(
                np.array([1, 2, 3]),
                filename,
                fmax='string')


def test_dynamic_spectrogram():
    with pytest.raises(ParameterError):
        audio.dynamic_spectrogram(1, 'filename')

    with pytest.raises(TypeError):
        audio.dynamic_spectrogram(
                np.array([1, 2, 3]),
                'filename',
                ref='something')


def test_process_audio():
    data_path = os.path.dirname(os.path.realpath(__name__))
    audio_file = data_path + '/audio_data/sine_44100_2ch.wav'

    with pytest.raises(TypeError):
        audio.process_audio(audio_file, 'something', 128, 22050, True)

    with pytest.raises(ValueError):
        audio.process_audio(audio_file, 1, 'something', 22050, True)

    with pytest.raises(TypeError):
        audio.process_audio(audio_file, 1, 128, 'something', True)
