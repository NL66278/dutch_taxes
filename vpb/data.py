"""All code to assist in Vpb Declaration."""
# Copyright 2019 - Ronald Portier - <ronald@portier.eu>.
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
# pylint: disable=too-few-public-methods
from dotmap import DotMap


class Data(DotMap):
    # pylint: disable=too-many-instance-attributes,too-many-ancestors

    def __init__(self):
        super().__init__()
        # Input data
        self.goodwill_initial = 0
        self.goodwill_yearly_amortisation = 0
        self.goodwill_years_amortisation = 0
        self.claims_on_owner = []
        self.owned_stock = 0
        self.bank_accounts = []
        self.reserved = 0
        self.initial_capital = 0
        self.reserved_profit_previous = 0
        self.nett_turnover = 0
        self.wages = 0
        self.pensionfund_reservations = 0
        self.labor_costs_various = 0
        self.other_costs_various = 0
        self.interest_received = []
        # Data to be computed
        self.total_claims_on_owner = 0
        self.total_claims_on_other = 0
        self.goodwill_remaining = 0
        self.intangible_assets = 0
        self.reserved_profit_current = 0
        self.profit_or_loss = 0
        self.liquidity = 0
        self.tangible_assets = 0
        self.total_assets = 0
        self.total_liabilities = 0
        self.total_labor_costs = 0
        self.total_amortisation = 0
        self.total_profit_non_financial = 0
        self.total_costs = 0
        self.end_capital = 0
