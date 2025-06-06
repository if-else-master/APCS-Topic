N,M = map(int,input().split())

num = []
bb = []

for i in range(N):
    aa = list(map(int,input().split()))
    bb.append(aa)
for j in range(len(bb)):    
    num.append(bb[j])

ans = []

for k in range(len(num)):
    ans.append(max(num[k]))
    


print(sum(ans))
point = sum(ans)
list_point = []

for h in range(len(ans)):
    if point % ans[h] == 0:
        list_point.append(ans[h])

if list_point == []:
    print("-1")
else:
    print(' '.join(map(str,list_point)))
    
print(N,M)
