# -*- coding: utf-8 -*-

""" Check recursively if all the files have a common samplerate.

Todo:
    - record the log into a file (in /var/log or /tmp where it makes the most
    sense
    - Reorder alphabetically the library calls
"""

# Extract the samplerate from the config file
import configparser
import os
import sys
from asc import utils
from soundfile import SoundFile
from logbook import Logger, StreamHandler

config_path = os.path.expanduser('~') + '/.ascrc'

log = Logger('My samplerate logger')
config = configparser.ConfigParser()
config.read(config_path)
samplerate = int(utils.read_config('audio', 'samplerate', config))
data_path = utils.read_config('path', 'data', config)

for root, dirs, files in os.walk(data_path):
    for f in files:
        if f.endswith('wav'):
            audio_file = SoundFile(os.path.join(root, f))
            if audio_file.samplerate != samplerate:
                StreamHandler(sys.stdout).push_application()
                log.warn('wrong samplerate %d - %s' % (
                    samplerate,
                    os.path.join(root, f)))
