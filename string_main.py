from Modules import StringUtil

print(StringUtil.formatTitle("Create String entity"))
s = StringUtil.String("Sam")
print(s)

print(StringUtil.formatTitle("Anagrams"))
print("Is Anagram: " + str(StringUtil.is_anagram("foo", "oof")))
print("Is Anagram: " + str(StringUtil.is_anagram("foo", "of")))
print("Is Anagram: " + str(StringUtil.is_anagram("sILENt", "lISTEN")))

