# coding=utf-8
import sys
n = int(sys.stdin.readline())
x = [int(i) for i in sys.stdin.readline().split()]
y = [int(i) for i in sys.stdin.readline().split()]
i = 0
tmp = 0
while(i < len(x)):
    flag = False
    if y[i] != 0 and x[i] < y[i]:
        j = 0

        while(j < len(x)):
            if x[j] != 0 and x[j] > y[j]:
                if i == j:
                    continue
                if j > i:
                    tmp += j-i
                    flag = True
                    break
                elif j < i:
                    tmp += i+j
                    flag = True
                    break
                x[j] -= 1
                x[i] += 1

            j+=1
    i+=1
    print(i)
    if flag:
        i-=1

print(tmp)