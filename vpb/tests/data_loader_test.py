"""Test Vpb Data Loader with hard coded data."""
# Copyright 2019 - Ronald Portier - <ronald@portier.eu>.
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
# pylint: disable=too-few-public-methods,no-self-use
from vpb.data import Data


class DataLoaderTest():

    def load(self):
        data = Data()
        data.company_assets_yearstart = 12000
        data.goodwill_initial = 80000
        data.goodwill_yearly_amortisation = 8000
        data.goodwill_years_amortisation = 5
        data.claims_on_owner = [
            ('mortgage', 20000),
            ('current account owner', 10000)]
        data.owned_stock = 12000
        data.bank_accounts = [
            ('current account', 8000),
            ('savings account', 4000)]
        data.reserved = 40000
        data.initial_capital = 18000
        data.reserved_profit_previous = 8000
        data.nett_turnover = 35000
        data.wages = 25000
        data.pensionfund_reservations = 2000
        data.labor_costs_various = 660
        data.other_costs_various = 1200
        data.interest_received = [
            ('current_account', 10),
            ('mortgage', 400),
            ('current account owner', 200)]
        return data
