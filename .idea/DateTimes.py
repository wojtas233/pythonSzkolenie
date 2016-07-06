#2016-07-04 17-00-00
from datetime import datetime
date1 = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
date1 = input('Wprowadz date 1: ')
date2 = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
data2 = input('Wprowadz date 2: ')

dt = date1 - date2
print(dt)
d = dt / 7

print(d)