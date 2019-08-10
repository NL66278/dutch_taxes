# Copyright 2019 - Ronald Portier - <ronald@portier.eu>.
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
import argparse

from vpb.data_loader_csv import DataLoaderCsv
from vpb.declaration import Declaration


def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('data_file')
    return parser.parse_args()


if __name__ == '__main__':
    ARGS = get_arguments()
    DATA_LOADER = DataLoaderCsv(ARGS.data_file)
    DECLARATION = Declaration(DATA_LOADER)
    DECLARATION.do_main()
