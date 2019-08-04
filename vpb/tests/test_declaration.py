# Copyright 2019 - Ronald Portier - <ronald@portier.eu>.
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
import unittest

from vpb.declaration import Declaration
from .data_loader_test import DataLoaderTest


class TestDeclaration(unittest.TestCase):

    def setUp(self):
        super().setUp()
        data_loader = DataLoaderTest()
        self.declaration = Declaration(data_loader)
        self.declaration.load()

    def test_declaration(self):
        self.declaration.do_main()

    def test_compute_goodwill(self):
        self.declaration.compute_goodwill()
        self.assertEqual(self.declaration.vpb_data.goodwill_remaining, 40000)


if __name__ == '__main__':
    unittest.main()
