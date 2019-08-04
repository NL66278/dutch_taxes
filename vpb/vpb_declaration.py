"""All code to assist in Vpb Declaration."""
# Copyright 2019 - Ronald Portier - <ronald@portier.eu>.
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).


class VpbDeclaration(object):
    """Load data for Vpb declaration, do cumputations, print report."""

    def do_main(self):
        """Drive the Vpb declaration report."""
        self.load()
        self.compute()
        self.report()

    def load(self):
        """Load data for a particular Vpb declaration."""
        raise NotImplementedError()

    def compute(self):
        """Do computations for a particular Vpb declaration."""
        raise NotImplementedError()

    def report(self):
        """Print report with all the lines to enter on the Vpb Declaration."""
        raise NotImplementedError()


if __name__ == '__main__':
    DECLARATION = VpbDeclaration()
    DECLARATION.do_main()
