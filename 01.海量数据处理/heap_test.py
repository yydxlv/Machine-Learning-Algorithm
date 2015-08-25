__author__ = 'xilin'
import heapq
def decorated_file(f):
        count, s = f
        yield (-count, s)  # cann't neglect '-'
a=range(1,10,2)
b=range(1,20,3)
c=[(2,'s'),(3,'w'),(8,'r'),(4,'q'),(5,'e')]
d=[(4,'q'),(5,'e')]
for i in heapq.merge(a,b):
    print(i)
for i in heapq.merge(*[decorated_file(f) for f in c]):
    print(i)
    # print(str(i))
print('\n')
for i in heapq.merge(c):
    print(i)
