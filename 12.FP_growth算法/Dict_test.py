__author__ = 'xilin'
a={'a':4,'b':2,'c':3}
print([v[0] for v in sorted(a.items(), key=lambda p: p[1], reverse=True)])
b=a.copy()
for k in a.keys():
    if a[k]>2:
        del b[k]
a=b.copy()

