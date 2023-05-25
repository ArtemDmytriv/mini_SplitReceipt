import src.party_event as pe
from src.expanse import Expanse
from src.person import Person
from src.transaction import Transaction
from src.currency_util import *

import sched
import uuid

if __name__ == "__main__":
    #sc = sched.scheduler()
    #ev = sc.enter(3, 1, schedule_rate_update)
    
    #sc.run()

    p1 = Person("Amogus")
    p2 = Person("Bobak")
    p3 = Person("Codik")

    ev = pe.GroupEvent(uuid.uuid1())
    ev.add_person(p1)
    ev.add_person(p2)
    ev.add_person(p3)

    ev.print_members()

    ex1 = Expanse("Fuel", 2000)
    ex1.set_rates([("Amogus", 0.6),("Bobak", 0.4)])
    p2.add_expanse(ex1)

    ex2 = Expanse("Food", 1250)
    ex2.set_equal_rates(list(map(lambda x : x.name, ev.members)))
    p3.add_expanse(ex2)

    ev.print_members()
    print(ex1.is_valid_rates())
    ev.calc_transition()

    ev.print_transactions()

    #ex1.set_equal_rates(["Amogus", "Bodad"])

    #print(ex1.is_valid_rates())

    #ev.print_members()
    #ev.calc_transition()



