import math
from Modules import StringUtil

print(StringUtil.formatTitle("Displaying Numbers and Strings"))
print(5 + 5, "foo", 3)

print(StringUtil.formatTitle("Multiply"))
print(5 * 3)

x = 5
x *= 3
print(x)

print(StringUtil.formatTitle("Division and Rounding"))
print(5 / 3)
print(round(5 / 3))
print(round(5 / 3, 1))

print(StringUtil.formatTitle("Float Division"))
print(5 / 3)

print(StringUtil.formatTitle("Integer Division"))
print(5 // 3)

print(StringUtil.formatTitle("Using a external Lib"))
print(math.ceil(5.6))
print(math.floor(5 / 3))

print(StringUtil.formatTitle("Powers"))
print(5 * 5 * 5)
print(5 ** 3)
print(math.pow(5, 3))

print(StringUtil.formatTitle("Modulus and Divide"))
print(5 / 3)
print(5 % 3)

print(StringUtil.formatTitle("Code format Numbers"))
print(100)
print(1000)
print(1_000)
print(1000000000)
print(1_000_000_000)

print(StringUtil.formatTitle("Range Builtin"))
for n in range(5, 12):
    print(n)


print(StringUtil.formatTitle("Range Builtin With Step"))
for n in range(5, 12, 2):
    print(n)


print(StringUtil.formatTitle("Divide by 50% until 0"))
number = 100
while number > 0:
    print(number)
    number //= 2
