# -*- coding: utf-8 -*-
# pylint: disable=wildcard-import, unused-wildcard-import, invalid-name, unused-import
""" A library of Paver extensions and generally useful task definitions for
    any Python project.

    Copyright © 2013 Jürgen Hermann
    Licensed under the Apache License, Version 2.0
"""
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import os
import re
import sys

from paver.easy import *
from paver.setuputils import setup
from setuptools import find_packages


#
# Project Description
#
projectdir = path(__file__).dirname().abspath()
changelog = (projectdir / "debian" / "changelog").text().decode("UTF-8")
project = dict(
    # project data & layout
    name = changelog.split()[0],
    version = re.search(r"(?<=\()[^)]+(?=\))", changelog).group(),
    package_dir = {"": "src"},
    packages = find_packages(projectdir / "src", exclude=["tests"]),
    test_suite = "nose.collector",
    zip_safe = True,
    include_package_data = True,
    data_files = [
        ("EGG-INFO", [
            "README.md", "LICENSE", "debian/changelog",
        ]),
    ],

    # dependency management
    install_requires = [
    ],
    setup_requires = [
        "docutils",
        "Sphinx",
    ],
    extras_require = {
    },

    # PyPI
    url = "https://github.com/jhermann/cobblestones",
    license = "Apache License Version 2.0",
    keywords = "python tool automation continuous.integration",
    author = u"Jürgen Hermann",
    author_email = "jh@web.de",
    description = __doc__.split('.')[0].strip().decode("UTF-8"),
    long_description = __doc__.split('.', 1)[1].strip().decode("UTF-8"),
    classifiers = [
        # values at http://pypi.python.org/pypi?:action=list_classifiers
        "Development Status :: 3 - Alpha",
        #"Development Status :: 4 - Beta",
        #"Development Status :: 5 - Production/Stable",
        "Operating System :: OS Independent",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.7",
        "Topic :: Software Development :: Build Tools",
        "Topic :: Software Development :: Quality Assurance",
        "Topic :: Utilities",
    ],
)


#
# Tasks
#
try:
    import cobblestones
except ImportError:
    # Special bootstrap in our own project, in absence of an initialized virtualenv
    sys.path.insert(0, projectdir / "src")
    import cobblestones


@task
@needs(["paver.misctasks.generate_setup", "paver.misctasks.minilib", "setuptools.command.develop"])
def init():
    """initial project setup"""
    # Fix paver-minilib bug
    import zipfile
    pml = zipfile.ZipFile("paver-minilib.zip", 'a')
    try:
        pml.getinfo("paver/version.py")
    except KeyError:
        pml.writestr("paver/version.py", "VERSION='0.0.0'\n")
    pml.close()


#
# Call back to Paver
#
setup(**project)

