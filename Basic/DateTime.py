from Modules import StringUtil
from datetime import datetime

print(StringUtil.formatTitle("ISO Weekday Value"))
d = datetime.now()
result = datetime.isoweekday(d)
print(result)

print(StringUtil.formatTitle("Current Date"))
d = datetime.now()
result = datetime.date(d)
print(result)
