# Copyright 2019 - Ronald Portier - <ronald@portier.eu>.
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
# pylint: disable=too-few-public-methods


class BaseFinanceFact():

    def __init__(self, key, parent_key):
        self.key = key
        self.parent_key = parent_key

    def get_value(self):
        raise NotImplementedError("You must use one of the derived classes.")


class BranchFinanceFact(BaseFinanceFact):

    def __init__(self, key, parent_key):
        super().__init__(key, parent_key)
        self.parent_key = parent_key
        self.nodes = {}  # Other branch or leave.

    def append_fact(self, fact):
        self.nodes[fact.key] = fact

    def get_value(self):
        value = 0
        for node in self.nodes.values():
            value = value + node.get_value()
        return value


class LeaveFinanceFact(BaseFinanceFact):

    def __init__(self, key, parent_key, value):
        super().__init__(key, parent_key)
        self.value = value

    def get_value(self):
        return self.value




class FinanceTree():

    def __init__(self):
        self.key = 'root'
        self.nodes = {}
        for node_key in TOPNODES:
            self.nodes[node_key] = BranchFinanceFact(node_key, self.key)
        self.node_lookup = {}

    def add_fact(self, fact):
        if fact.key in self.node_lookup:
            raise AttributeError(
                "Key %s already present in tree." % fact.key)
        if fact.parent_key not in self.node_lookup:
            raise AttributeError(
                "Parent key %s must be added before key %s." %
                (fact.parent_key, fact.key))
        self.node_lookup[fact.key] = fact
        self.node_lookup[fact.parent_key].append_fact(fact)
