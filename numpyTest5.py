from numpy import *

a=arange(6)
print(a)

b=arange(12).reshape(4,3)
print(b)

c=arange(24).reshape(2,3,4)
print(c)
set_printoptions(threshold=10000)
print(arange(10000).reshape(100,100))