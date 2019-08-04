# Copyright 2019 - Ronald Portier - <ronald@portier.eu>.
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
import os
import unittest

from vpb.data_loader_csv import DataLoaderCsv


class TestDataLoaderCsv(unittest.TestCase):

    def test_loader(self):
        script_dir = os.path.dirname(__file__)
        datafile = "test_data.csv"
        datafile_path = os.path.join(script_dir, datafile)
        data_loader = DataLoaderCsv(datafile_path)
        data = data_loader.load()
        self.assertEqual(data.goodwill_initial, 80000)
        self.assertEqual(data.bank_accounts[0], ("bank_accounts", 8000))
        self.assertEqual(data.bank_accounts[1], ("saving_account", 4000))


if __name__ == '__main__':
    unittest.main()
