from Modules import StringUtil

print(StringUtil.formatTitle("Using a List"))
numbers_a = [1, 2, 3, 4, 5]
numbers_a[2] = 6

# The next code would error because of immutability
# print(StringUtil.formatTitle("Tuples"))
# numbers_b = (1, 2, 3, 4, 5)
# numbers_b[2] = 6


print(StringUtil.formatTitle("Tuple methods: .count()"))
numbers_c = (1, 2, 3, 4, 5, 2)
print(
    numbers_c.count(2)
)



