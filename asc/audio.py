# -*- coding: utf-8 -*-
import librosa
import librosa.display
import librosa.feature
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


def dynamic_spectrogram(data, display=False):
    """ Compute the spectrogram of a time serie of samples.

    The dynamic spectrogram is obtained by computing the the signal in the
    frequency domain and display the spectrogram.

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


def static_spectrogram(
        data,
        mel_bands=128,
        fmax=22050,
        x_axis='time',
        y_axis='mel',
        display=False):
    """ Compute the static spectrogram of a time serie of samples.

    The static spectromgram is computed by take the power of the signal in the
    frequency domain according a decomposition in mel bands and a maximum
    frequency.

    Args:
        data (array): 1D array of audio data.
        mel_bands (int): number of mel bands for the decomposition
        fmax (int): maximum frequency (in Hertz).
        display (boolean): plotting or saving the output figure.

    Returns:
        None

    Todo:
        - remove the padding/margin around the plot
        - Add a path and a name where to save the plots

    Note:
        Need to ensure that the computation is accurate

    """

    data_freq_power = np.abs(librosa.stft(data))**2
    librosa.feature.melspectrogram(
            S=data_freq_power,
            power=2.0,
            n_mels=mel_bands,
            fmax=fmax)

    librosa.display.specshow(
            librosa.power_to_db(data_freq_power, ref=np.max),
            y_axis=y_axis,
            x_axis=x_axis,
            fmax=fmax)

    if display:
        plt.ylabel('Mel')
        plt.xlabel('Time [samples]')
        plt.show()


def process_audio(filename, frame_size, mel_bands, fmax, display):
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
            dynamic_spectrogram(y, display=display)
            static_spectrogram(y, mel_bands, fmax, display=display)
