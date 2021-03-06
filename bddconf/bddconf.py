# -*- coding: utf-8 -*-

from typing import List
from collections import OrderedDict
import openpyxl
import math

from dd import autoref as _bdd

class Attribute:

    def __init__(self, code: str, name: str, *values: List[str]):
        self.code = code
        self.name = name
        self.values = values

    def len(self):
        return len(self.values)

    def size(self, base=2):
        return math.floor(math.log(self.len() - 1, base)) + 1

    def decompose(self) -> (List, OrderedDict, List):
        """

        Returns:
            (variables, mapping, rules)

            mapping: List
            mapping: OrderedDict "attribute.code:attribute.values.get(value)" --> (var1, val1), (var2, val2)
            invalid_values: List

        """
        vars = tuple("{}_{:d}".format(self.code, n)
               for n in range(self.size()))
        mapping = OrderedDict()
        invalid_values = []
        for n, val in enumerate(self.values):
            tag = "{code}:{n:0{width}d}".format(code=self.code,
                                                n=n, width=self.size(base=10))
            values = self._binary_representation(n)
            mapping[tag] = tuple(zip(vars, values))
        # Mark the unused value as invalid
        # Get the max used value
        max_used_val = self.len() - 1
        # Get the max possible value according to bit size
        max_val = 2 ** self.size() - 1
        for n in range(max_used_val + 1, max_val + 1):
            invalid_value = []
            for n, k in enumerate(self._binary_representation(n)):
                atom = vars[n]
                if not k:
                    atom = "~{}".format(atom)
                invalid_value.append(atom)
            invalid_value = " /\ ".join(invalid_value)
            invalid_values.append(invalid_value)
        return vars, mapping, invalid_values

    def _binary_representation(self, n, width=None):
        if width is None:
            width = self.size()
        return tuple(map(int, "{n:0{width}b}".format(n=n, width=width)))

    def __repr__(self):
        return "{code}-{name}[{size:{width}d}]".format(code=self.code,
                                                       name=self.name,
                                                       size=self.len(),
                                                       width=self.size(base=10))


class ConfigBDD:

    def __init__(self):
        self.attributes = []
        self.variables = []
        self.mapping = None
        self.invalid_values = None
        self.bdd = None

    def append_attribute(self, attribute: Attribute):
        self.attributes.append(attribute)

    def decompose(self):
        """Decomposes an attribute in binary variables
        """
        mapping_dict = OrderedDict()
        invalid_values = []
        vars = []
        for attr in self.attributes:
            attr_vars, attr_mapping, attr_invalid_values = attr.decompose()
            mapping_dict.update(attr_mapping)
            if attr_invalid_values:
                invalid_values.extend(attr_invalid_values)
            vars.extend(attr_vars)
        self.variables = vars
        self.mapping = mapping_dict
        self.invalid_values = invalid_values

    def init_bdd(self):
        self.decompose()
        self.bdd = _bdd.BDD()
        for var in self.variables:
            self.bdd.add_var(var)
        for expr in self.invalid_values:
            self.bdd.add_expr(expr)

    def add_expr(self, expr, **kwargs):
        return self.bdd.add_expr(expr, **kwargs)

    def parse_workbook(self, filename: str):
        ws = openpyxl.load_workbook(filename).worksheets[0]
        for col in ws.iter_cols():
            attr = Attribute(col[0].value, col[1].value)
            vals = [c.value for c in col[2:] if c.value]
            attr.values = vals
            self.append_attribute(attr)
