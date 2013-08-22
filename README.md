# cobblestones

## Overview
*cobblestones* adds often-used tasks and helper functions on top of
[Paver](https://pypi.python.org/pypi/Paver).


## Documentation

The documentation for the current GitHub master source is located at
[github.io](http://jhermann.github.io/cobblestones/).


## Contributing

*cobblestones* is obviously written in [Python](http://www.python.org/),
and the documentation is generated using [Sphinx](https://pypi.python.org/pypi/Sphinx).
Paver is used to build and manage the project, and *cobblestones* eats its own dogfood
(see `pavement.py`).

To set up a working directory, follow these steps:

    git clone https://github.com/jhermann/cobblestones.git
    cd cobblestones
    virtualenv --no-site-packages .
    . bin/activate
    pip install -r requirements.txt
    paver init

*cobblestones* can also be found on [PyPI](https://pypi.python.org/pypi/cobblestones)
and [Ohloh](https://www.ohloh.net/p/cobblestones).


## License

*cobblestones* is released under the 
[Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0.html),
see LICENSE for details.

