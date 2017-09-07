.. highlight:: shell

============
Installation
============


Stable release
--------------

To install Acoustic Scene Classification, run this command in your terminal:

.. code-block:: console

    $ pip install asc

This is the preferred method to install Acoustic Scene Classification, as it
will always install the most recent stable release. 

If you don't have `pip`_ installed, this `Python installation guide`_ can guide
you through the process.

.. _pip: https://pip.pypa.io
.. _Python installation guide: http://docs.python-guide.org/en/latest/starting/installation/

Requirements
^^^^^^^^^^^^

In order to properly work you need to satisfy several dependencies:

- tkinter (python 2 or 3 depending of your system)
- libsndfile

For example on Debian:

.. code-block:: console
  
  $ sudo apt-get install libsndfile python-tk

If you still have issues at the installation, you can still refer to the
:doc:`faq` or post an issue on the `Github repo`_.

From sources
------------

The sources for Acoustic Scene Classification can be downloaded from the `Github repo`_.

You can either clone the public repository:

.. code-block:: console

    $ git clone git://github.com/mattberjon/asc

Or download the `tarball`_:

.. code-block:: console

    $ curl  -OL https://github.com/mattberjon/asc/tarball/master

Once you have a copy of the source, you can install it with:

.. code-block:: console

    $ python setup.py install


.. _Github repo: https://github.com/mattberjon/asc
.. _tarball: https://github.com/mattberjon/asc/tarball/master
