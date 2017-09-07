=====
FAQ
=====

Error at the installation on Fedora and python 2.7
--------------------------------------------------

The package is using several libraries that need to be compiled in order to work
properly as they aren't 100% python. If you get an error such as

.. code-block:: console 
  gcc: error: /usr/lib/rpm/redhat/redhat-hardened-cc1: No such file or directory

You can try to resolve the issue by installation the package `redhat-rpm-config`.
