from person import Person

class Expanse:
    def __init__(self, exp_name: str):
        self.exp_name = exp_name
        self.amount = 0
        #self.currency = 'UAH'


class GroupEvent:
    def __init__(self) -> None:
        self.members = []
        self.money = []

    def add_member(self, person: Person) -> None:
        self.members.append(person)

    def print_members(self) -> None:
        print(", ".join(self.members))



