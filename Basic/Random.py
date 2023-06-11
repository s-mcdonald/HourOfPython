import random

from Modules import StringUtil


print(StringUtil.formatTitle("Random"))
my_list = ["foo", "bar", "baz"]

print(random.choice(my_list))

random.shuffle(my_list)

print(my_list)
