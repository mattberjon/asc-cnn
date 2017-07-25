# -*- coding: utf-8 -*-

""" Data module

This module lets the program to download the data from the server.

"""
import os
import requests
import sys
import time
import zipfile

class Data(object):
    """ Data collection.
    """
    
    def __init__(self):
        pass

    def get_data(self):
        pass

    def unzip_data(self):
        pass

    def clear_zip(self):
        pass


tmp_dir = '/tmp'
dest_dir = 'data'

urls = ['https://zenodo.org/record/400515/files/TUT-acoustic-scenes-2017-development.audio.1.zip',
'https://zenodo.org/record/400515/files/TUT-acoustic-scenes-2017-development.audio.2.zip',
'https://zenodo.org/record/400515/files/TUT-acoustic-scenes-2017-development.audio.3.zip',
'https://zenodo.org/record/400515/files/TUT-acoustic-scenes-2017-development.audio.4.zip',
'https://zenodo.org/record/400515/files/TUT-acoustic-scenes-2017-development.audio.5.zip',
'https://zenodo.org/record/400515/files/TUT-acoustic-scenes-2017-development.audio.6.zip',
'https://zenodo.org/record/400515/files/TUT-acoustic-scenes-2017-development.audio.7.zip',
'https://zenodo.org/record/400515/files/TUT-acoustic-scenes-2017-development.audio.8.zip',
'https://zenodo.org/record/400515/files/TUT-acoustic-scenes-2017-development.audio.9.zip',
'https://zenodo.org/record/400515/files/TUT-acoustic-scenes-2017-development.audio.10.zip']

other_data = [
        'https://zenodo.org/record/400515/files/TUT-acoustic-scenes-2017-development.doc.zip',
        'https://zenodo.org/record/400515/files/TUT-acoustic-scenes-2017-development.error.zip'
        ]

def downloader(url, path):
    elem_nb = len(url)
    counter = 0

    for elem in url:
        filename = elem.split('/')[-1]

        with open(path + '/' + filename, 'wb') as f:
            start = time.clock
            r = requests.get(elem, stream=True)
            dl = 0
            file_size = int(r.headers['Content-length'])
            if file_size is None:
                f.write(r.conent)
            else:
                counter += 1
                for chunk in r.iter_content(chunk_size=1024):
                    dl += len(chunk)
                    f.write(chunk)
                    done = int(50 * dl / file_size)
                    sys.stdout.write("\r%s/%d [%s%s]" % (counter, elem_nb, '=' * done, ' ' * (50-done)) )
                    sys.stdout.flush()

        print('')
    return 1

def unziper(filenames, origin_dir, dest_dir):
    """

    Args:
        filenames: a list of strings containing the filenames
        origin_dir: directory where are stored the files
        dest_dir: directory where the files will be extracted
    """

    for elem in filenames:
        print(elem)
        zip_ref = zipfile.ZipFile(origin_dir + '/' + elem, 'r')
        zip_ref.extractall(dest_dir)
        zip_ref.close()

def cleaner(filenames, path):
    for elem in filenames:
        os.remove(path + '/' + elem)
        print("%s deleted" % elem)



dlw = downloader(other_data, tmp_dir)
if dlw:
    print('Download complete')

filenames = []
for elem in other_data:
    filenames.append(elem.split('/')[-1])

print('Unzipping of the files')
unziper(filenames, tmp_dir, dest_dir)

print('Cleaning of the downloaded files')
cleaner(filenames, tmp_dir)
