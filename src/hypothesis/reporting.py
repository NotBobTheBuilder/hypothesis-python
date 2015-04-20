# coding=utf-8

# Copyright (C) 2013-2015 David R. MacIver (david@drmaciver.com)

# This file is part of Hypothesis (https://github.com/DRMacIver/hypothesis)

# This Source Code Form is subject to the terms of the Mozilla Public License,
# v. 2.0. If a copy of the MPL was not distributed with this file, You can
# obtain one at http://mozilla.org/MPL/2.0/.

# END HEADER

from __future__ import division, print_function, absolute_import, \
    unicode_literals

import inspect

from hypothesis.utils.dynamicvariables import DynamicVariable
from hypothesis.settings import Settings, Verbosity
from hypothesis.internal.compat import text_type
from hypothesis.errors import InvalidArgument


def silent(value):
    pass


def default(value):
    print(value)


reporter = DynamicVariable(default)


def current_reporter():
    return reporter.value


def with_reporter(new_reporter):
    return reporter.with_value(new_reporter)


def current_verbosity():
    return Settings.default.verbosity


def to_text(textish):
    if inspect.isfunction(textish):
        textish = textish()
    if not isinstance(textish, text_type):
        raise InvalidArgument(
            "Invalid type for reporting. Expected %s but got %s" % (
                text_type.__name__, type(textish).__name__,))
    return textish


def verbose_report(text):
    if current_verbosity() >= Verbosity.verbose:
        current_reporter()(to_text(text))


def report(text):
    if current_verbosity() >= Verbosity.normal:
        current_reporter()(to_text(text))
