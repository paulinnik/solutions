# Задание №2 про Васю и расписание
from itertools import *

k = 0
for comb in product('ФМИРО', repeat=7):
    schedule = ''.join(comb)
    if schedule.count('ФИ') == 0 and schedule.count('ИФ') == 0 and len(set(schedule)) == 5 and schedule.count('О') == 2:
        k += 1
print(k)
