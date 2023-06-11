import math
from Modules import StringUtil

print(StringUtil.formatTitle("Basic String"))
print("Hello World")

print(StringUtil.formatTitle("String formatting"))
for name in ["foo", "bar"]:
    print(f"Hello {name}")
    print("Hello {0:s}".format(name))
    print("Hello {0}".format(name))
    print()

print(StringUtil.formatTitle("Multiline String"))
multi_line_string = """
this is a multiline \
string that will
display text on
multiple lines
"""
print(multi_line_string)

print(StringUtil.formatTitle("String output with numbers"))
print(5 + 5, "foo", 3)

print(StringUtil.formatTitle("String intrinsic functions"))
print("foo".upper())
print("foo".capitalize())
print("foo".lower())
