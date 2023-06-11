from Modules import StringUtil

print(StringUtil.formatTitle("Booleans"))
temp = int(input("Enter the temperature in Celsius: "))

if temp > 30:
    print("The temp is a hot day")
elif temp > 20:
    print("It is a nice day")
else:
    print("It is cold today")

x = 0
while x <= 10:
    print(x)
    x += 1
