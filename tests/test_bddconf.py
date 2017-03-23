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


<<<<<<< HEAD
def test_parse_workbook():
    config = bddconf.ConfigBDD()
    config.parse_workbook(INFILE)
    for attr in config.attributes:
        print(attr)
    assert False
=======
def test_parse_workbook(worksheet):
    bddconf.
>>>>>>> fe9561d9437af8402234486f9e600a542726eb25
