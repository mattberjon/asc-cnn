=====
Usage
=====

It is possible to use ASC loading the library and integrates it into your current
project. You can as well using the command line to use it as it is.

Command line
------------

Several commands are available and can be obtained using::

    $ asc --help

In order to setup properly the project, I would recommend to run the setup
command as follow::

    $ asc setup

You'll be asked to enter the root path where you want to store the data.
Then you can download the data using the command::

    $ asc getdata

You can take a coffee and wait until archives are downloaded and the audio
files extracted into the audio folder.

Library import
--------------

To use Acoustic Scene Classification in a project::

    import asc


