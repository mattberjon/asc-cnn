# -*- coding: utf-8 -*-

"""Main module."""

import numpy as np
from scipy import signal
import matplotlib.pyplot as plt


def spectrogram(frequency, sampling_rate, smp_len):
    x = np.arange(smp_len)
    sine = np.sin(2 * np.pi * frequency * x / sampling_rate)
    f, t, Sxx = signal.spectrogram(sine, sampling_rate)
    return f, t, Sxx


def plot_spectrogram(f, t, Sxx):
    plt.pcolormesh(t, f, Sxx)
    plt.ylabel('Frequency [Hz]')
    plt.xlabel('Time [samples]')
    plt.show()
