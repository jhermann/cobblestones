#! /bin/bash
set -e
set -x
venv=1.9.1
if test ! -f bin/activate; then
    mkdir -p build
    (cd build \
        && curl -sOkS https://pypi.python.org/packages/source/v/virtualenv/virtualenv-$venv.tar.gz \
        && tar xfz virtualenv-$venv.tar.gz )
    python build/virtualenv-$venv/virtualenv.py --no-site-packages .
    bin/pip install -r requirements.txt
    bin/paver init
fi

set +x; . bin/activate; set -x
paver build
paver doc
