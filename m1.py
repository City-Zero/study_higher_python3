# coding=utf-8
import sys
x = sys.stdin.readline().strip('\n')
l = []
for i in x:
    l.append(int(x)+5 % 10)
l[0],l[3] = l[3],l[0]
l[1],l[2] = l[2],l[1]
for i in l:
    print(i,end='')