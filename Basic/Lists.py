from Modules import StringUtil

list_a = ["foo", "bar", "baz", "qux"]

print(StringUtil.formatTitle("Direct access to list"))
print(list_a[0])
print(list_a[1])
print(list_a[2])
print(list_a[3])

print(StringUtil.formatTitle("Iterate over list"))
for x in list_a:
    print(x)

print(StringUtil.formatTitle("Negative index"))
print(list_a[-1])
print(list_a[-2])
print(list_a[-3])
print(list_a[-4])
# print(list_a[-5]) # index out of range error

print(StringUtil.formatTitle("Sub list"))
print(list_a[1:3])

print(StringUtil.formatTitle("Add Element"))
list_a.append("biz")
list_a.insert(2, "inserted")
for x in list_a:
    print(x)

print(len(list_a))
