# coding=utf-8
import sys
s = int(sys.stdin.readline().strip('\n'))
for _ in range(s):
    l = list(map(int, sys.stdin.readline().strip('\n').split()))
    n = l[0]
    l = l[1:]
    ls = []
    con = len(l)
    for i in range(con):
        for j in range(i+1,con):
            ls.append([l[i],l[j]])
    ls = sorted(ls,key=lambda x:x[0]/x[1])
    print(ls)
    print(ls[n-1][0],ls[n-1][1])