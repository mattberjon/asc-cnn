=======
History
=======

0.3.1 (2017-08-22)
------------------

Added
^^^^^

* `Issue #8`_: config file feature
* `Issue #11`_: Samplerate setting up through CLI
* `Issue #10`_: Spectrogram calculation
* `Issue #24`_: Add a 'config' subcommand to the CLI
* `Issue #25`_: Read a value from the config file
* `Issue #21`_: Script to verify the samplerate sanity of the database
* `Issue #30`_: Function to transform milliseconds to samples

Changed
^^^^^^^

* `Issue #23`_: Update of the documentation for the installation process
* `Issue #26`_: Update of the CLI subcommand 'getdata' 
* `Issue #32`_: Exception handling in config reading

Deprecated
^^^^^^^^^^

Nothing.

Removed
^^^^^^^

Nothing.

Fixed
^^^^^

* `Issue #9`_: trailing slash on data path
* `Issue #13`_: Update of the config file parameters
* `Issue #15`_: Crash when setting up the samplerate
* `Issue #22`_: Update of the dependency list
* `Issue #25`_: Update of the config file
* Update of docstrings
* Update of the documentation

Security
^^^^^^^^

* Update of the Coveralls library from 1.1 to 1.2.0

0.2.3 (2017-08-07)
------------------

Added
^^^^^

* Travis config file
* pytest suite
* CLI tests
* `issue #5`_: Package coverage for the development setup
* `issue #6`_: adding of a `clear_zip()` to clean the archive files

Changed
^^^^^^^

* Python 3.3 testing removed

Deprecated
^^^^^^^^^^

* Nothing

Removed
^^^^^^^

* Nothing

Fixed
^^^^^

* `Issue #4`_: invalid functools dependency
* `Issue #7`_: update of docstring `unzip_data()`

Security
^^^^^^^^

* Nothing


0.2.2 (2017-07-31)
------------------

Added
^^^^^

* nothing

Changed
^^^^^^^

* Updated of the ChangeLog (HISTORY.rst)

Deprecated
^^^^^^^^^^

* nothing

Removed
^^^^^^^

* nothing

Fixed
^^^^^

* nothing

Security
^^^^^^^^

* nothing

0.2.1 (2017-07-31)
------------------

Added
^^^^^
* nothing

Changed
^^^^^^^

* nothing

Deprecated
^^^^^^^^^^

* nothing

Removed
^^^^^^^

* nothing

Fixed
^^^^^

* unzip_data() url list issue
* download of temporary files in the right directory  

Security
^^^^^^^^

* nothing

0.2.0 (2017-07-31)
------------------

Added
^^^^^

* Adding of a documentation (with docstrings)
* CLI command to download and unzip data automatically
* creation of a python package
* configuration of Tox
* download() method in data class

Changed
^^^^^^^

* Use of RST instead of markdown for all the documentation
* development packages are now in requirements_dev.txt

Deprecated
^^^^^^^^^^
* nothing

Removed
^^^^^^^

* nothing

Fixed
^^^^^

* source files satisfy PEP8
* bug fix on getdata cli

Security
^^^^^^^^

* Update of all packages to their latest versions

0.1.0 (2017-07-25)
------------------

* First release as a package.


.. _Issue #4: https://github.com/mattberjon/asc-cnn/issues/4
.. _Issue #7: https://github.com/mattberjon/asc-cnn/issues/7
.. _Issue #5: https://github.com/mattberjon/asc-cnn/issues/5
.. _Issue #6: https://github.com/mattberjon/asc-cnn/issues/6
.. _Issue #9: https://github.com/mattberjon/asc-cnn/issues/9
.. _Issue #8: https://github.com/mattberjon/asc-cnn/issues/8
.. _Issue #13: https://github.com/mattberjon/asc-cnn/issues/13
.. _Issue #15: https://github.com/mattberjon/asc-cnn/issues/15
.. _Issue #11: https://github.com/mattberjon/asc-cnn/issues/11
.. _Issue #10: https://github.com/mattberjon/asc-cnn/issues/10
.. _Issue #22: https://github.com/mattberjon/asc-cnn/issues/22
.. _Issue #23: https://github.com/mattberjon/asc-cnn/issues/23
.. _Issue #24: https://github.com/mattberjon/asc-cnn/issues/24
.. _Issue #25: https://github.com/mattberjon/asc-cnn/issues/25
.. _Issue #26: https://github.com/mattberjon/asc-cnn/issues/26
.. _Issue #21: https://github.com/mattberjon/asc-cnn/issues/21
.. _Issue #30: https://github.com/mattberjon/asc-cnn/issues/30
.. _Issue #32: https://github.com/mattberjon/asc-cnn/issues/32
