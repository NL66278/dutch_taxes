# Copyright 2019 - Ronald Portier - <ronald@portier.eu>.
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
import unittest

from vpb.vpb_declaration import VpbDeclaration


class TestVpbDeclaration(unittest.TestCase):

    def setUp(self):
        super().setUp()
        self.declaration = VpbDeclaration()

    def test_declaration(self):
        self.declaration.report()


if __name__ == '__main__':
    unittest.main()
