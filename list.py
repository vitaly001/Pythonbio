__author__ = 'Vitaly'
L1 = [1, 2, 3, 3, 4]
L2 = [3, 4, 5, 6]
L3 = [i for i in set(L1) if i in L2]
print(type(L3))
print(L3)