import sys,re
l1 = sys.stdin.readline().strip('\n')
l2 = sys.stdin.readline().strip('\n')
l2 = l2.replace('?','.')
s = set()
while l1:
    z = re.findall(l2,l1)
    s = s | set(z)
    l1 = l1[1:]
print(len(s))