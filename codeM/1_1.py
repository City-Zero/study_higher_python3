# coding=utf-8
import sys
(n,m) = [int(i) for i in sys.stdin.readline().split()]
item = []
for _ in range(n):
    (a,b) = [int(i) for i in sys.stdin.readline().split()]
    b = 0.8 if b == 1 else 1
    item.append([a,b])

rate = []
for _ in range(m):
    (a, b) = [int(i) for i in sys.stdin.readline().split()]
    rate.append([a, b])

rate = sorted(rate,key=lambda i:i[1],reverse=True)

price = sum([i[0] for i in item])
for i in rate:
    if price >= i[0]:
        price = price - i[1]
        break

e_p = sum([i[0]*i[1] for i in item])
print('%.2f' % min(e_p,price))


