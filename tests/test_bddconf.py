#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_bddconf
----------------------------------

Tests for `bddconf` module.
"""

import pytest
from bddconf import bddconf

import openpyxl


INFILE = "tests/test_shirts.xlsx"


def test_parse_workbook(worksheet):
    bddconf.
