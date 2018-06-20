# coding=utf-8
import sys

data = {'A':[0,1],
        'D':[0,2],
        'G':[1,0],
        'J':[1,1],
        'M':[1,2],
        'P':[2,0],
        'T':[2,1],
        'W':[2,2],
        }
last = []
for i in range(65,91):
    c = chr(i)
    if data.get(c,None):
        last = data.get(c,None)
    else:
        data[c] = last

n = int(sys.stdin.readline())

def length(a,b):
    if not a:
        a = [0,0]
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

for i in range(n):
    s = sys.stdin.readline().strip()
    la = None
    step = 0
    for i in s:
            step += length(la,data.get(i))
            la = data.get(i)

    print(step)