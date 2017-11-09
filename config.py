import os
import tempfile

basedir = os.path.abspath(os.path.dirname(__file__))


class App:
    __conf = {
            'CONFIG_PATH': os.path.abspath(os.path.expanduser('~')) + '/.ascrc',
            'URL_PATH': os.path.join(basedir, 'samples/url_list.txt'),
            'TMP_PATH': tempfile.gettempdir()
            }

    @staticmethod
    def config(name):
        return App.__conf[name]
