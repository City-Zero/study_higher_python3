# coding=utf-8
import sys

def fuc(x,y):
    i = y
    t = 0
    a = b = 1;
    while i and x:
        a *= x;
        i-=1
        x-=1
    while y:
        b*=y
        y -=1

    t = a//b
    return t

n = int(sys.stdin.readline())
for _ in range(n):
    s = sys.stdin.readline().strip()
    sum = 0
    start = 1
    l = len(s)
    for it in range(l):
        sum += fuc(26,it)
    for jt in range(1,l+1)[:-1]:
        it = start
        while it<ord(s[l-jt]):
            sum = fuc(26-it,jt-1)
        start = s[len-jt] - 'a' +2
    print(sum+1)