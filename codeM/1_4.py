# coidng=utf-8
import sys
import copy
'''
n:n名选手
m:m轮比赛
k:前k晋级
C:0-C之间的分数
'''
(n,m,k,C) = (int(i) for i in sys.stdin.readline().split())
ml = [int(i) for i in sys.stdin.readline().split()]
s = sum(ml)
for i in range(m):
    ml[i] = ml[i] / s
t = 0
tt = 0
a_l = []
for i in range(n):
    e_l = [int(i) for i in sys.stdin.readline().split()]
    if -1 in e_l:
        t = i
        for j in range(len(e_l)):
            if e_l[j] == -1:
                tt = j
                break
    a_l.append(e_l)
a_l[t][tt] = 0

m_1 = []
for index,i in enumerate(a_l):
    power = sum([k1*k2 for k1,k2 in zip(i,ml)])
    m_1.append([index,power])

diff = a_l[t]
diff[tt] = C
power = sum([k1*k2 for k1,k2 in zip(diff,ml)])
m_2 = copy.deepcopy(m_1)
m_2[t][1] = power
m_1 = sorted(m_1,key=lambda i:i[1],reverse=True)
m_2 = sorted(m_2,key=lambda i:i[1],reverse=True)
#print(m_1,m_2)
a_1 = [2] * n
a_2 = [2] * n
flag = m_1[k]
pp = k
# 找到k之前不同于k的下标pp
while pp>=0:
    if m_1[k][1] == m_1[pp][1]:
        pp -= 1
    else:
        break
# 无需随机选择人
if pp+1 == k:
    for i in m_1[0:k]:
        a_1[i[0]] = 1
# 需要随机T人
else:
    # 之前的人通过
    for i in m_1[0:pp+1]:
        a_1[i[0]] = 1
    gg = k
    # 选出k之后第一个不同于K的下标gg
    while gg < len(m_1):
        if m_1[k][1] == m_1[gg][1]:
            gg += 1
        else:
            break
    # 这些人是游客能获胜
    for i in m_1[pp+1:gg]:
        a_1[i[0]] = 3
#print(a_1)

flag = m_2[k]
pp = k
# 找到k之前不同于k的下标pp
#print(m_2)
while pp>=0:
    if m_2[k][1] == m_2[pp][1]:
        pp -= 1
    else:
        break
# 无需随机选择人
#print(pp)
if pp+1 == k:
    for i in m_2[0:k]:
        a_2[i[0]] = 1
# 需要随机T人
else:
    # 之前的人通过
    for i in m_2[0:pp+1]:
        a_2[i[0]] = 1
    gg = k
    # 选出k之后第一个不同于K的下标gg
    while gg < len(m_2):
        if m_2[k][1] == m_2[gg][1]:
            gg += 1
        else:
            break
    # 这些人是游客能获胜
    for i in m_2[pp+1:gg]:
        a_2[i[0]] = 3
z = []
#print(a_1,a_2)
for i,j in zip(a_1,a_2):
    if i==j:
        z.append(i)
    else:
        z.append(3)
[print(i) for i in z]