from .currency_util import *

import logging
logger = logging.getLogger(__name__)

class Expanse:
    def __init__(self, exp_name: str = "", amount: float = 0.0, currency: str = "UAH"):
        self.exp_name = exp_name
        self.amount = amount
        self.currency = currency
        self.devided_by: dict[str:float] = {}    #{ "name" : portion -> None means all equals??? }

    def get_amount_in(self, currency: str):
        return self.amount * convert_rate(self.currency, currency)

    def convert_to(self, currency: str):
        self.amount = convert_rate(self.currency, currency) * self.amount
        self.currency = currency

    def set_rates(self, rates : list[tuple]):
        for name, rate in rates:
            self.devided_by[name] = rate
    
    def set_equal_rates(self, names : list[str]):
        for name in names:
            self.devided_by[name] = 1.0 / len(names)

    def is_valid_rates(self) -> bool:
        return round(sum(self.devided_by.values())) == 1.0

    def __str__(self) -> str:
        return f"{self.amount}_{self.currency} : {self.devided_by}"