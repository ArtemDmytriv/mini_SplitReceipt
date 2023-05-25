from src.person import Person

import logging
logger = logging.getLogger(__name__)

class Transaction:
    def __init__(self, from_person, to_person):
        self.sender = from_person
        self.receiver = to_person
        self.amount = 0.0
        self.done = False

    def __str__(self) -> str:
        if (len(self.sender.name) and len(self.receiver.name)):
            return f"Transaction: {self.sender.name} -({self.amount})-> {self.receiver.name}"
        return "Transaction: Not fully filled"
