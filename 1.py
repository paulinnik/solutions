# Задание №1 про Гермиону
from itertools import *
k=0
for comb in permutations('АБОМЖК'):
    name=''.join(comb)
    if name[0]!='А' and name.count('АО')==0 and name.count('ОА')==0:
        k+=1
print(k)