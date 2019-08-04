"""All code to assist in Vpb Declaration."""
# Copyright 2019 - Ronald Portier - <ronald@portier.eu>.
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).


class VpbDeclaration(object):
    """Load data for Vpb declaration, do cumputations, print report."""

    def do_main(self, args):
        """Drive the Vpb declaration report."""
        self.load_data()
        self.do_computations()
        self.report()

    def report(self):
        """Print report with all the lines to enter on the Vpb Declaration."""
        raise NotImplementedError()
