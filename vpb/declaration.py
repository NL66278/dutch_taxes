# Copyright 2019 - Ronald Portier - <ronald@portier.eu>.
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
# pylint: disable=too-few-public-methods,no-self-use


class Declaration():
    """Load data for Vpb declaration, do cumputations, print report."""

    def __init__(self, loader):
        """Initialisation."""
        self.loader = loader
        self.vpb_data = None

    def do_main(self):
        """Drive the Vpb declaration report."""
        self.load()
        self.compute()
        self.report()

    def load(self):
        """Load data for a particular Vpb declaration."""
        self.vpb_data = self.loader.load()

    def compute(self):
        """Do computations for a particular Vpb declaration."""
        data = self.vpb_data
        self.compute_goodwill()
        self.compute_intangible_assets()
        self.compute_financial_assets()
        data.profit_or_loss = data.end_capital - data.initial_capital

    def compute_goodwill(self):
        data = self.vpb_data
        data.goodwill_remaining = \
            data.goodwill_initial - (
                data.goodwill_yearly_amortisation *
                data.goodwill_years_amortisation)

    def compute_intangible_assets(self):
        data = self.vpb_data
        data.intangible_assets = data.goodwill_remaining

    def compute_financial_assets(self):
        data = self.vpb_data
        data.total_claims_on_owner = data.bank_accounts[1][1]
        data.total_financial_assets = \
            data.owned_stock + data.total_claims_on_owner

    def report(self):
        """Print report with all the lines to enter on the Vpb Declaration."""
        data = self.vpb_data
        self.print_start_lines()
        self.print_intangible_assets()
        self.print_financial_assets()
        self._print_data_line(
            "Resultaat gewone bedrijfsuitoefening", data.profit_or_loss)

    def print_start_lines(self):
        data = self.vpb_data
        print("")
        self._print_data_line(
            "Fiscaal ondernemingsvermogen begin boekjaar",
            data.company_assets_yearstart)

    def print_intangible_assets(self):
        data = self.vpb_data
        self._print_sub_header("Immateriële vaste activa")
        self._print_data_line(
            "Goodwill", data.goodwill_remaining)

    def print_financial_assets(self):
        data = self.vpb_data
        self._print_sub_header("Financiële vaste activa")
        self._print_data_line(
            "Deelnemingen", data.owned_stock)
        self._print_data_line(
            "Langlopende vorderingen op participanten",
            data.total_claims_on_owner)
        self._print_data_line(
            "Totaal financiële vaste activa",
            data.total_financial_assets)

    def _print_data_line(self, text, amount):
        print("{0:<70}{1:>10}".format(text, amount))

    def _print_sub_header(self, text):
        print("{0:-<80}".format('-'))
        print(text)
        print("{0:-<80}".format('-'))
