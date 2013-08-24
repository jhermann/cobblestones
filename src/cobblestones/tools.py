# -*- coding: utf-8 -*-
""" Helpers for writing pavements.
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

from paver.options import Bunch


def bunchify(obj, _seen=None):
    """ Recursively convert all dicts found in `obj` to Paver bunches.

        That includes `obj` itself; if it's already a Bunch, the original
        object is returned. Replacement of inner dicts by `Bunch` objects
        happens in-place. Other dict-like objects are scanned, but their
        type is retained.
    """
    _seen = _seen or {}
    if id(obj) in _seen:
        return _seen[id(obj)]
    _seen[id(obj)] = obj

    if type(obj) is dict:
        _seen[id(obj)] = Bunch(obj)
        obj = _seen[id(obj)]

    try:
        items = obj.iteritems
    except AttributeError:
        pass # obj is not a dict-like object
    else:
        for key, val in items():
            obj[key] = bunchify(val, _seen)

    return obj

