__author__ = 'Vitaly'
def compute(n,x,y):
    if n==0 : return x
    return compute(n-1,x+y,y)

print(compute(-3, 4, 5))