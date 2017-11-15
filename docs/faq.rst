=====
FAQ
=====

Error at the installation on Fedora/Debian and python 2.7
---------------------------------------------------------

The package is using several libraries that need to be compiled in order to work
properly as they aren't 100% python. If you get an error such as

.. code-block:: console 

  gcc: error: /usr/lib/rpm/redhat/redhat-hardened-cc1: No such file or directory

You can try to resolve the issue by installation the package `redhat-rpm-config`,
or `build-essential` on Debian based flavours.

tkinter.TclError: no display name and no $DISPLAY environement variable
-----------------------------------------------------------------------

If for some reasons you run this program on machine without XWindow, you will
most probably encounter this error. It exists a workaround by specifying to
Matplotlib which backend you want to use. Most probably you'll use the default
backend called Agg. In order to do that, you need to edit the `matplotlibrc`
file located on GNU/Linux in `~/.config/matplotlib/matplotlibrc`.

You will need to edit or add the following line:

.. code-block:: console

  backend   : Agg

If you don't use GNU/Linux or want further information about this particular
setup, I advise you to visit the `Matplotlib documentation`_.

.. _Matplotlib documentation: https://matplotlib.org/users/customizing.html#the-matplotlibrc-file
