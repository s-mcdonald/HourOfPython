def formatTitle(title: str):
    prefix = "\n\n"
    underline = "-" * len(title)
    return prefix + title.strip().capitalize() + "\n" + underline


def is_anagram(str1: str, str2: str) -> True | False:
    return True if sorted(str1.lower().strip()) == sorted(str2.lower().strip()) else False


class String:
    def __new__(cls, in_s):
        obj = super().__new__(cls)
        obj.str = in_s
        return obj

    def __init__(self, in_s: str):
        self.str = in_s

    def __str__(self):
        return self.str

    def format(self):
        return formatTitle(self.str)

    def myNameIs(self):
        return "My name is: " + self.str

    def is_anagram(self, str2: str) -> True | False:
        return is_anagram(self.str, str2)
