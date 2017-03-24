#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_bddconf
----------------------------------

Tests for `bddconf` module.
"""
from collections import OrderedDict

import pytest
from bddconf import bddconf

import dd.autoref as _bdd


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

def test_decompose(configuration: bddconf.ConfigBDD):
    a, b, c  = configuration.attributes
    configuration.decompose()
    variables = ['A001_0',
                 'A001_1',
                 'A001_2',
                 'A002_0',
                 'A002_1',
                 'A003_0']
    invalid_values = ['A001_0 /\ A001_1 /\ ~A001_2',
                      'A001_0 /\ A001_1 /\ A001_2']
    mapping = OrderedDict([('A001:0', (('A001_0', 0), ('A001_1', 0), ('A001_2', 0))),
                           ('A001:1', (('A001_0', 0), ('A001_1', 0), ('A001_2', 1))),
                           ('A001:2', (('A001_0', 0), ('A001_1', 1), ('A001_2', 0))),
                           ('A001:3', (('A001_0', 0), ('A001_1', 1), ('A001_2', 1))),
                           ('A001:4', (('A001_0', 1), ('A001_1', 0), ('A001_2', 0))),
                           ('A001:5', (('A001_0', 1), ('A001_1', 0), ('A001_2', 1))),
                           ('A002:0', (('A002_0', 0), ('A002_1', 0))),
                           ('A002:1', (('A002_0', 0), ('A002_1', 1))),
                           ('A002:2', (('A002_0', 1), ('A002_1', 0))),
                           ('A002:3', (('A002_0', 1), ('A002_1', 1))),
                           ('A003:0', (('A003_0', 0),)),
                           ('A003:1', (('A003_0', 1),))])
    assert configuration.variables == variables
    assert configuration.invalid_values == invalid_values
    assert configuration.mapping == mapping


def test_bdd(configuration):
    bdd = _bdd.BDD()
    bdd.add_var("x")
    bdd.add_var("y")
    bdd.add_var("z")
    bdd.dump("tests/out/out.pdf")
    pass
