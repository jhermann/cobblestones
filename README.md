# cobblestones ![Logo](https://raw.github.com/jhermann/cobblestones/master/doc/_static/cobblestones-logo-48.png)

| **Travis** | **Jenkins** |
|:-------------:|:-------------:|
| [![Travis Status](https://travis-ci.org/jhermann/cobblestones.png?branch=master)](https://travis-ci.org/jhermann/cobblestones) | [![Jenkins Status](http://huschteguzzel.de/hudson/buildStatus/icon?job=cobblestones)](http://huschteguzzel.de/hudson/view/jhermann/job/cobblestones/) |


## Overview
*cobblestones* adds often-used tasks and helper functions on top of
[Paver](https://pypi.python.org/pypi/Paver).


## Documentation

The documentation for the current GitHub master source is regularly published to
[github.io](http://jhermann.github.io/cobblestones/).

A [continuously built document tree](http://huschteguzzel.de/hudson/job/cobblestones/doclinks/1/)
with the latest changes is also available.


## Contributing

*cobblestones* is obviously written in [Python](http://www.python.org/),
and the documentation is generated using [Sphinx](https://pypi.python.org/pypi/Sphinx).
Paver is used to build and manage the project, and *cobblestones* eats its own dogfood
(see `pavement.py`).

To set up a working directory, follow these steps:

```sh
git clone "https://github.com/jhermann/cobblestones.git"
cd "cobblestones"
./jenkins.sh
. bin/activate
pip install -M -r tools-requirements.txt
```

*cobblestones* can also be found on [PyPI](https://pypi.python.org/pypi/cobblestones)
and [Ohloh](https://www.ohloh.net/p/cobblestones).


## License

*cobblestones* is released under the 
[Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0.html),
see LICENSE for details.

