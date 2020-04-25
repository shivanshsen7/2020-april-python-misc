"""
Created on Sat Apr 25 12:03:03 2020

@author: shivanshsen7@gmail.com
"""
n = int(input().strip())
sequence = list()
for x in range(1, n+1):
    for y in str(x):
        sequence.append(y)
print(sequence[n])