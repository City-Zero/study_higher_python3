# coding=utf-8
import sys
s = sys.stdin.readline().strip('\n')
N = int(sys.stdin.readline().strip('\n'))
for _ in range(N):
    l = list(map(int,sys.stdin.readline().strip('\n').split()))
    count = 0
    for i in s:
        count += 1
        if i == 'u':
            l[2] -= 1
            if l[2] == 0:
                break
        elif i == 'd':
            l[2] += 1
            if l[2] > l[0]:
                break
        elif i == 'l':
            l[3] -= 1
            if l[3] == 0:
                break
        elif i == 'r':
            l[3] += 1
            if l[3] > l[1]:
                break
    print(count)