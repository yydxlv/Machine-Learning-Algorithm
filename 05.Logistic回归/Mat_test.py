__author__ = 'xilin'
import pprint
from numpy import array
mm=array([1,1,1])
pp=array([1,2,3])
print(pp+mm)
print(pp*2)
print(pp**2)
jj=array([[1,2,3],[3,4,5]])
print(jj)
print(jj[0])
print(jj[0][1]) # 2
print(jj[0,1])  # 2

# Matrix
from numpy import mat,matrix
ss=mat([1,2,3])
print(type(ss),":",ss)
mm=matrix([1,2,3])
print(mm)
Pylist=[5,15,20]
print(mat(Pylist))
print(ss*mm.T)
print(mm.transpose())
import matplotlib.pyplot as plt
from numpy import *
fig = plt.figure()
ax = fig.add_subplot(111)
x = arange(-3.0, 3.0, 0.1)
# y = [2*i for i in x]
y = [(4.12+0.48*i)/0.61 for i in x]
ax.plot(x, y)
plt.xlabel('X1');plt.ylabel('X2')
plt.show()
# y = [(-weights[0]-weights[1]*i)/weights[2] for i in x]
