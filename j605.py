num = int(input())
ts = []

for i in range(num):
    a = list(map(int,input().split()))
    ts.append(a)

ht = [-2]
tr = []
time = []

for j in range(num):
    if ts[j][1] > ht[0]:
        ht = [ts[j][1]]
        time = [ts[j][0],ts[j][1]]
    else:
        continue

for k in range(num):
    if ts[k][1] == -1:
        tr.append(ts[j][1])

b = len(tr)*2

if ht[0]-num-b > 0:
    print(ht[0]-num-b,time[0])
else:
    print(ht[0],time[0])
