from Modules import StringUtil

print(StringUtil.formatTitle("Booleans"))
print(3 > 6)
print(3 < 6)

price = 100
print(price < 200 and price > 0)
print(200 > price > 0)

print(not price > 200)
# or
# and
# not

print(StringUtil.formatTitle("IN operator"))
mylist = [1, 2, 3, 4, 5]
print(1 in mylist)

