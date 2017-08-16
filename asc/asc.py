# -*- coding: utf-8 -*-

"""Main module."""

from scipy import signal
import matplotlib.pyplot as plt
from soundfile import SoundFile, blocks as sfblocks


def spectrogram(data, sampling_rate):
    """ Compute the spectrogram of a time serie of samples.

    The dynamic spectrogram is computed using the `spectrogram()` function
    provided by Scipy.

    Args:

    Returns:
        f: Array of sample frequencies
        t: Array of segment times
        Sxx: Spectrogram of the signal

    Todo:
        - be able to read the input of any signal given

    """
    f, t, Sxx = signal.spectrogram(data, sampling_rate)
    return f, t, Sxx


def plot_spectrogram(f, t, Sxx, plot=True, filename='nothing.png'):
    """ Plot/Save the current figure.

    Display or save the dynamic spectrogram according.

    Args:
        f: Array of sample frequencies
        t: Array of segment times
        Sxx: Spectrogram of the signal
        plot: Flag to plot or save the figure

    Todo:
        - Save the filename to the data folder with the right name
        - ensure to create each figure independently before showing or saving
        them

    """
    plt.pcolormesh(t, f, Sxx)
    plt.ylabel('Frequency [Hz]')
    plt.xlabel('Time [samples]')
    if plot:
        plt.show()
    else:
        plt.savefig(filename)


def audio_metadata(filename, frame_size=9, display_plot=False):
    """ extract audio metadata and compute the dynamic spectrogram.

    Prepare the audio file and process it to compute the dynamic spectrograms
    block by block.

    Args:
        filename (str): Path to the audio file.
        frame_size (int): frame size for the "per block" processing.
        display_plot (boolean): display or save the plot.

    Returns:
        Nothing

    Todo:
        - check if the samplerate of the file corresponds to the samplerate
        in the configuration file

    """
    chunk = 512
    audio_file = SoundFile(filename)
    af_chan_nb = audio_file.channels
    af_samplerate = audio_file.samplerate
    
    for block in sfblocks(filename, blocksize=chunk):
        # separate the channels to compute the spectrograms
        block_left = block[:, 0]
        block_right = block[:, 1]
        # Compute the dynamic spectrogram
        f_left, t_left, Sxx_left = spectrogram(block_left, 44100)
        f_right, t_right, Sxx_right = spectrogram(block_right, 44100)
        # Plot the spectrogram
        plot_spectrogram(f_left, t_left, Sxx_left, display_plot)
        plot_spectrogram(f_right, t_right, Sxx_right, display_plot)


def process_audio():
    """ Process an audio file

    Process the audio file and extract the metadata such as:

    - load the audio file
    - extract the right meta data (samplerate, channel nb, length of the file)
    - check if the samplerate corresponds to the config file
    - compute the right nb of frames to compute
    - process the dynamic spectrogram
    - process the static spectrogram
    - save the images to the right folder

    """
    pass
