# coding=utf-8
import sys
(n,m) = [int(x) for x in sys.stdin.readline().strip('\n').split()]
machine = []
arr = []
task = []
tmp = []
for _ in range(n):
    arr.append(None)
    tmp.append([int(x) for x in sys.stdin.readline().strip('\n').split()])
tmp = sorted(tmp,key=lambda x:x[0])
s = 0
e = 0
while e < len(tmp):
    if tmp[e][0] == tmp[s][0] and e < len(tmp) -1:
        e+=1
    else:
        if e == len(tmp) - 1:
            e+=1
        t= sorted(tmp[s:e],key=lambda x:x[1],reverse=True)
        [machine.append(x) for x in t]
        s = e
tmp.clear()
for _ in range(m):
    tmp.append([int(x) for x in sys.stdin.readline().strip('\n').split()])
tmp = sorted(tmp,key=lambda x:x[0])
s = 0
e = 0
while e < len(tmp):
    if tmp[e][0] == tmp[s][0] and e < len(tmp) -1:
        e+=1
    else:
        if e == len(tmp) - 1:
            e+=1
        t= sorted(tmp[s:e],key=lambda x:x[1],reverse=True)
        [task.append(x) for x in t]
        s = e
tmp.clear()
# print(machine,task)
i = 0
j = 0
ret = 0
count = 0
while i < len(arr):
    flag = None
    while j < len(task):
        if machine[i][0] >= task[j][0] and machine[i][1] >= task[j][1]:
            flag = j
            # print("1")
            j+=1
            break
        elif machine[i][1] < task[j][1]:
            j+=1
        else:
            break
    # print(flag)
    if flag is not None:
        # print("2")
        ret += 200 * task[flag][0] + 3*task[flag][1]
        count +=1
        j = flag+1
    i+=1
print("%s %s"%(count,ret))