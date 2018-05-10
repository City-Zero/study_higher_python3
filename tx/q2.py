import sys
n = int(sys.stdin.readline().strip('\n'))
m = sys.stdin.readline().strip('\n').split()
count = 0
for i in m:
    t = i
    while len(t) > n:
        t = t[n-1:]
        count += 1
    if len(t) != 0:
        count+=1
print(count)