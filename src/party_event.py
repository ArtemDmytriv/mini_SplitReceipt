from .person import Person
from .transaction import Transaction
from .expanse import Expanse

from pprint import pprint
import logging
logger = logging.getLogger(__name__)

class GroupEvent:
    def __init__(self, id) -> None:
        self.id = id
        self.members: list[Person] = []
        self.transactions: list[Transaction] = []

    def add_person(self, person: Person) -> None:
        if person.name in map(lambda x : x.name, self.members):
            print("Err insert: The same name already exist")
            return
        self.members.append(person)

    def get_person(self, name: str) -> Person:
        idx = None
        try:
            temp = list(map(lambda x : x.name, self.members))
            idx = temp.index(name)
        except ValueError as ve:
            print("Err get: Person not exist in Group")
        return self.members[idx] if idx != None else Person("")

    def get_total_expanse(self) -> float:
        return sum( sum(exp.amount for exp in p.expanses) for p in self.members)

    def print_members(self) -> None:
        pprint([ str(p) for p in self.members ])
    
    def print_transactions(self) -> None:
        pprint([ str(p) for p in self.transactions ])

    def add_expanse(self, name: str, val: Expanse):
        self.get_person(name).add_expanse(val)

    def calc_transition(self):
        for memb in self.members:
            for expanse in memb.expanses:
                for sender, rate in expanse.devided_by.items():
                    tr = Transaction(self.get_person(sender), memb)
                    tr.amount = expanse.amount * rate
                    self.transactions.append(tr)

        # remove self-to-self transition
        self.transactions = list(filter(lambda x : x.sender != x.receiver, self.transactions))

        
        pass
