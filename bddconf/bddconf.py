# -*- coding: utf-8 -*-

from typing import List
<<<<<<< HEAD
from collections import OrderedDict
=======
>>>>>>> fe9561d9437af8402234486f9e600a542726eb25
import openpyxl


class Attribute:

    def __init__(self, code: str, name: str, *values: List[str]):
        self.code = code
        self.name = name
        self.values = values

    def size(self):
        return len(self.values)

    def nbit(self):
        return len(bin(self.size())) - 2

    def __repr__(self):
        return "{code}-{name}[{size:03d}]".format(code=self.code,
                                                  name=self.name,
                                                  size=self.size())


class ConfigBDD:

    def __init__(self):
        self.attributes = []
<<<<<<< HEAD
        self.variables = []
=======
>>>>>>> fe9561d9437af8402234486f9e600a542726eb25
        self.mapping = None
        self.rules = None

    def append_attribute(self, attribute: Attribute):
        self.attributes.append(attribute)

<<<<<<< HEAD
    def decompose(self):
        """Decompose in binary variables
        """
        for attr in self.attributes:
            variables = ["{}_{:06d}".format(attr.code,
                                            n) for n in range(attr.nbit())]
            mapping = OrderedDict()
            for n, val in enumerate(attr.values):
                tag = "{code}:{n:03}".format(code=attr.code,
                                             n=n)


=======
>>>>>>> fe9561d9437af8402234486f9e600a542726eb25
    def parse_workbook(self, filename: str):
        ws = openpyxl.load_workbook(filename).worksheets[0]
        for col in ws.iter_cols():
            attr = Attribute(col[0].value, col[1].value)
            vals = [c.value for c in col[2:] if c.value]
            attr.values = vals
            self.append_attribute(attr)
