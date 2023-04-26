from .person import Person
from pprint import pprint

class GroupEvent:
    def __init__(self) -> None:
        self.members = []
        self.money = []

    def add_member(self, person: Person) -> None:
        self.members.append(person)

    def print_members(self) -> None:
        lst = [ str(p) for p in self.members ]
        pprint(lst)



