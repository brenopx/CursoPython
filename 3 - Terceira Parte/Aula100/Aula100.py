"""
Aula 100 - Datetime - Trabalhondo com data e hora em Python
https://docs.python.org/3.0/library/datetime.html
"""
from datetime import datetime, timedelta

# data = datetime(2019, 4, 20, 10, 53, 20)
# print(data.strftime('%d/%m/%Y  %H:%M:%S'))

# data = datetime.strptime('20/04/2019', '%d/%m/%Y')
# print(data.timestamp())

# data = datetime.fromtimestamp(1555729200.0)
# print(data)

# strptime(str, formato)
# .strftime(formato)
# timestamp
# fromtimestamp()

# data = datetime.strptime('20/04/1987 20:00:00', '%d/%m/%Y %H:%M:%S')
# data = data + timedelta(days=5, seconds=2*60*60)
# print(data.strftime('%d/%m/%Y  %H:%M:%S'))

d1 = datetime.strptime('20/04/1987 20:00:00', '%d/%m/%Y %H:%M:%S')
d2 = datetime.strptime('25/04/1987 22:33:00', '%d/%m/%Y %H:%M:%S')
dif = d2 - d1
print(dif)
print(dif.seconds)
print(dif.total_seconds())
print(dif.days)
print(d1.time())
print(d1 > d2)


