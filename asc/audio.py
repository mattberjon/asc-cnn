# -*- coding: utf-8 -*-
import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np
from soundfile import SoundFile, blocks as sfblocks


def extract_audio_data(filename):
    """ extract audio metadata and compute the dynamic spectrogram.

    Prepare the audio file and process it to compute the dynamic spectrograms
    block by block.

    Args:
        filename (str): Path to the audio file.

    Returns:
        The samplerate and number of channels.

    Todo:
        - check if the samplerate of the file corresponds to the samplerate
        in the configuration file

    """
    audiofile = SoundFile(filename)
    af_chan_nb = audiofile.channels
    af_samplerate = audiofile.samplerate

    return af_chan_nb, af_samplerate


def spectrogram(data, display=False):
    """ Compute the spectrogram of a time serie of samples.

    The dynamic spectrogram is computed using the `spectrogram()` function
    provided by Scipy.

    Args:
        data (array): 1D array of audio data.
        display (bool): Boolean to plot or save the current spectrogram.

    Returns:
        None

    Todo:
        - remove the padding/margin around the plot
        - Add a path and a name where to save the plots

    """
    data_freq = librosa.stft(data)
    data_freq_db = librosa.amplitude_to_db(data_freq, ref=np.max)
    librosa.display.specshow(data_freq_db)

    if display:
        plt.ylabel('Frequency [Hz]')
        plt.xlabel('Time [samples]')
        plt.show()
    else:
        plt.save()


def process_audio(filename, frame_size, display):
    """ act audio metadata and compute the dynamic spectrogram.

    Prepare the audio file and process it to compute the dynamic spectrograms
    block by block.

    Args:
        filename (str): Path to the audio file.
        frame_size (int): frame size for the "per block" processing.
        display_plot (boolean): display or save the plot.

    Returns:
        None

    Todo:
        - check if the samplerate of the file corresponds to the samplerate
        in the configuration file

    Note:
        According to the 2016 base line code, the frame size is 40ms with
        a hop size of 50%.

    """
    samples = librosa.frames_to_samples(frame_size)
    chan_nb, samplerate = extract_audio_data(filename)

    for block in sfblocks(filename, blocksize=samples[0]):
        # separate the channels to compute the spectrograms
        for chan in np.arange(chan_nb):
            if chan_nb < 2:
                y = block
            else:
                y = block[:, chan]
            # Compute the dynamic spectrogram
            #  y = block[:, chan]
            spectrogram(y, display=True)
