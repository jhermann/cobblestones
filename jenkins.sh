#! /bin/bash
set -e
set -x

# Bootstrap virtualenv if missing
venv=1.9.1
if test ! -f lib/.complete; then
    mkdir -p build/virtualenv
    rm -rf build/virtualenv
    if test ! -f build/virtualenv-$venv.tar.gz; then
        if pip install --log build/venv.log -M -d build virtualenv==$venv; then
            echo "Downloaded virtualenv-$venv.tar.gz using pip"
        else
            ( cd build && curl -sOkS https://pypi.python.org/packages/source/v/virtualenv/virtualenv-$venv.tar.gz )
        fi
    fi
    ( cd build && tar xfz virtualenv-$venv.tar.gz && mv virtualenv-$venv virtualenv )
    rm -rf "bin" "lib" "include" "local" || :
    python build/virtualenv/virtualenv.py --no-site-packages .
    bin/pip install --log build/pip.log -M -r requirements.txt
    bin/pip install -M --src lib -e git+https://github.com/jhermann/paver.git#egg=Paver
    bin/paver init
    bin/pip install -M yolk
    touch lib/.complete
fi

# Activate virtualenv and do your thing
set +x; . bin/activate; set -x
yolk -a
paver build
paver doc

