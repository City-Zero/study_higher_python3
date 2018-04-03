# coding=utf-8
import sys

n = int(sys.stdin.readline())
s = sys.stdin.readline()
exp = []
ops = []
d = {
    '+':1,
    '-':1,
    '*':2,
    '/':2
}
for i in s.split():


    if i in '+-*/':
        while len(ops) >= 0:
            if len(ops) == 0:
                ops.append(i)
                break
            o = ops.pop()
            if o == '(' or d[i] > d[o]:
                ops.append(o)
                ops.append(i)
                break
            else:
                exp.append(o)
    elif i == '(':
        ops.append(i)
    elif i == ')':
        while len(ops) > 0:
            o = ops.pop()
            if o == '(':
                break
            else:
                exp.append(o)
    else:
        exp.append(i)


while len(ops) > 0:
    exp.append(ops.pop())
print(' '.join(exp))