
class Person:
    def __init__(self, name: str) -> None:
        self.name = name
        self.expansed = 0 
        self.spend = 0

    def __str__(self) -> str:
        return f"{self.name} = [+{self.expansed},-{self.spend}]"
