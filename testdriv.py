import src.party_event as pe
from src.person import Person

if __name__ == "__main__":
    ev = pe.GroupEvent()
    ev.add_member(Person("Amogus"))
    ev.add_member(Person("Abobus"))

    ev.print_members()

