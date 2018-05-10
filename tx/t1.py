import sys
N = int(sys.stdin.readline().strip('\n'))
for _ in range(N):
    l = list(map(int,sys.stdin.readline().strip('\n').split()))
    print(l[1])