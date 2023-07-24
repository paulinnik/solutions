# Задание №3 про Шерлока и сейф
from itertools import *

k = 0
for comb in product('01235689', repeat=6):
    p = ''.join(comb)
    if p[0] == '2' and int(p[0]) % 3 != int(p[1]) % 3 and int(p[1]) % 3 != int(p[2]) % 3 and int(p[2]) % 3 != int(p[3]) % 3 \
            and int(p[3]) % 3 != int(p[4]) % 3 and int(p[4]) % 3 != int(p[5]) % 3:
        k += 1
print(k)
