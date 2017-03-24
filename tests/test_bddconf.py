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

@pytest.fixture()
def configuration():
    config = bddconf.ConfigBDD()
    config.parse_workbook(INFILE)
    return config


def test_parse_workbook(configuration):
    a, b, c  = configuration.attributes
    assert a.name == "Size"
    assert b.name == "Color"
    assert c.name == "Sex"
    assert a.code == "A001"
    assert b.code == "A002"
    assert c.code == "A003"
    assert a.len() == 6
    assert b.len() == 4
    assert c.len() == 2
    assert a.size() == 3
    assert b.size() == 2
    assert c.size() == 1

def test_decompose(configuration):
    a, b, c  = configuration.attributes
    configuration.decompose()
    pass
