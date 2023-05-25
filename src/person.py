from .expanse import Expanse

class Person:
    def __init__(self, name: str) -> None:
        self.name = name
        self.expanses: list[Expanse] = [] 

    def add_expanse(self, ex: Expanse):
        self.expanses.append(ex)

    def __str__(self) -> str:
        return f"{self.name} = [+{[str(exp) for exp in self.expanses]}]"
