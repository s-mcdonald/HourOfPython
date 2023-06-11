def add(a: int | float, b: int | float) -> int | float:
    return a + b


def sub(a: int | float, b: int | float) -> int | float:
    return a - b


def mul(a: int | float, b: int | float) -> int | float:
    return a * b


def div(a: int | float, b: int | float) -> int | float:
    return a / b


class BasicCalculator:
    def __new__(cls):
        print("Constructing the Calculator object...")
        obj = super().__new__(cls)
        obj.ex_list = []
        return obj

    def __init__(self):
        print("Initializing the Calculator object...")
        self.ex_list = []
