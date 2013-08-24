# -*- coding: utf-8 -*-
# pylint: disable=wildcard-import, unused-wildcard-import, invalid-name, unused-import
""" A library of Paver extensions and generally useful task definitions.

    This is the main build script for Paver.
"""
# Copyright © 2013 Jürgen Hermann
#
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
try:
    import cobblestones
except ImportError:
    # Special bootstrap in our own project, in absence of an initialized virtualenv
    sys.path.insert(0, projectdir / "src")
    import cobblestones
from cobblestones import tools

changelog = (projectdir / "debian" / "changelog").text("UTF-8")
project = tools.bunchify(cobblestones.pkg_info())
project.update(
    # TODO: find ways to get at these during runtime, within "cobblestones.pkg_info"
    version = re.search(r"(?<=\()[^)]+(?=\))", changelog).group(), # DRY principle
    packages = find_packages(projectdir / "src", exclude=["tests"]),
)


#
# Tasks
#

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
# Sphinx Documentation
#
# TODO: move to cobblestones.easy.documentation, and make project layout configurable (cf. options.sphinx)
@task
def doc():
    """create documentation"""
    # TODO: Use paver.doctools.html
    htmldir = projectdir / "build" / "doc" / "html"
    path("doc/api").rmtree()
    sh("sphinx-apidoc -f -o %s %s " % (
        projectdir / "doc" / "api",
        ' '.join([projectdir / "src" / pkg for pkg in project["packages"]]),
    ))
    #path("build/doc/html").rmtree()
    sh("make -f %s html" % (projectdir / "doc" / "ument"))
    sh("markdown2 README.md >%s/README.html" % htmldir)


@task
@needs("doc")
def browse():
    """create documentation and view in browser"""
    import webbrowser
    webbrowser.open("build/doc/html/index.html")


@task
@needs("doc")
def publish():
    """create documentation and publish to gh-pages branch"""
    import shutil

    workdir = projectdir / "build" / "gh-pages"
    htmldir = projectdir / "build" / "doc" / "html"
    origin = sh("git config --get remote.origin.url", capture=True).strip()

    workdir.rmtree(); workdir.makedirs()
    with pushd(workdir):
        # Specifically checkout gh-pages
        sh("git init")
        sh("git remote add -t gh-pages -f origin '%s'" % origin)
        sh("git checkout gh-pages")

        # Merge updated docs into existing branch
        for docfile in path(htmldir).walkfiles():
            # Skip junk files
            if any(docfile.endswith(i) for i in ("~", ".swp", ".tmp")):
                continue

            # Copy the updated file and register it for the commit
            # ("git add" will ignore unchanged files)
            dstfile = path(docfile.replace(htmldir, '.'))
            dstfile.parent.exists() or dstfile.parent.makedirs()
            shutil.copy2(docfile, dstfile)
            sh("git add '%s'" % dstfile)

        # Push it!
        sh("git status")
        sh("git commit -m 'Docs published by paver publish'")
        sh("git push origin gh-pages")
        sh("git status")


@task
def publish_init():
    """create orphaned gh-pages branch"""
    workdir = projectdir / "build" / "gh-pages"
    origin = sh("git config --get remote.origin.url", capture=True).strip()

    workdir.rmtree()
    sh("git clone -q '%s' %s" % (origin, workdir))
    with pushd(workdir):
        sh("git checkout --orphan gh-pages")
        sh("git rm -rf .")
        path(".nojekyll").write_text("Sphinx generated\n")
        sh("git add .nojekyll")
        sh("git commit -a -m 'Initialized by paver publish_init'")
        sh("git push origin gh-pages")


#
# Continuous Integration
#

@task
@needs(["build", "doc"])
def travis_ci():
    """continuous integration tasks for Travis"""


#
# Register with Paver
#
setup(**project)

