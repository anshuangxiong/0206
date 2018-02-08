from numpy import *

A=array([[1,1],[0,1]])
B=array([[2,0],[3,4]])
print(A*B)
print(dot(A,B))

a=ones(3,dtype=int32)
b=linspace(0,pi,3)
print(b)
print(A.sum())


a=floor(10*random.random((3,4)))
print(a)
print(a.shape)
print(a.ravel())
print(a.transpose())
print(vstack((A,B)))
print(hstack((A,B)))