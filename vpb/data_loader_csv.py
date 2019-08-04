"""All code to assist in Vpb Declaration."""
# Copyright 2019 - Ronald Portier - <ronald@portier.eu>.
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
# pylint: disable=too-few-public-methods,no-self-use
import csv

from .data import Data


ARRAY_INPUT = [
    'claims_on_owner', 'bank_accounts', 'interest_received']


class DataLoaderCsv():

    def __init__(self, datafile):
        self.datafile = datafile

    def load(self):
        # pylint: disable=no-self-use
        data = Data()
        with open(self.datafile, newline='') as csvfile:
            datareader = csv.reader(csvfile, delimiter=';', quotechar='"')
            row_count = 0
            for row in datareader:
                row_count = row_count + 1
                if row_count == 1:
                    continue  # Skip first row
                category = row[1]
                key = row[2].strip()  # account
                value = int(row[3])  # ridiculous that int() is needed...
                if category in ARRAY_INPUT:
                    data[category].append((key, value))
                else:
                    data[key] = value
        return data
