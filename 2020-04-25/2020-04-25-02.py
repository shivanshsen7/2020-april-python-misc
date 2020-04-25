"""
Created on Sat Apr 25 13:04:58 2020

@author: shivanshsen7@gmail.com
"""
def inlist(ls):
    ls = ls[1:-1].split(',')
    sub = list()
    out = list()
    for x in ls:
       for y in x:
           if y.isdigit():
               sub.append(int(y))
    out = [(sub[x], sub[x+1]) for x in range(0,5,2)]
    return out

def line(pnt):
    x = list(_[0] for _ in pnt)
    y = list(_[1] for _ in pnt)
    t1 = (x[1] - x[0]) * (y[2] - y[0])
    t2 = (x[2] - x[0]) * (y[1] - y[0])
    m = not(t1 - t2 == 0)
    return m

ip = input()
ls = inlist(ip)
print(line(ls))
