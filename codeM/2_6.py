# coding=utf-8
import sys

def chu(a,b):
    t = a // b
    a = a - b*t
    yield
    while True:
        a = a * 10
        t = a // b
        yield str(t)
        a = a - b * t
x,y = [int(x) for x in sys.stdin.readline().split()]
c = sys.stdin.readline().strip()
cc = c[::-1]
for i in range(0,len(cc)):
    if cc[i] != '0':
        break
c = c[:len(c)-i]
s = chu(x,y)
s.send(None)
start = 1
p = 0
while True:
    if p == len(c):
        break
    x = s.send(None)
    if c[p] == x:
        p += 1
    else:
        p = 0
    start += 1
    if start > 1000:
        start = 0
        break
if start == 0:
    print('-1')
else:
    print(start-len(c))