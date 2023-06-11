from Modules import StringUtil


class Foo:
    def __init__(self):
        print("Initializing the Calculator object...")
        self.ex_list = []


print(StringUtil.formatTitle("Get Types"))
print(type("a string"))
print(type(123))
print(type(123.456))
print(type(Foo()))
print(type(True))
print(type(False))
