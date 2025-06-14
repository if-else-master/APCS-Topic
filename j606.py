K,Q,R = map(int,input().split())

abc = list(str(input()))

Ans = []
temp = []
text = []

for i in range(Q):
    Ans.append(list(map(int,input().split())))
    if K != Q :
        Ans[i].remove(K)

if len(abc) != Q:
    del abc[-1]
for k in range(Q):
    for j in range(Q):
        Ans[k][j] = Ans[k][j]-1
    

#print(Ans)
#print(Ans[0][0],Ans[0][1])
#temp.insert(Ans[0][0],abc[0])
#temp.insert(Ans[0][1],abc[1])
#print(temp)

for item in range(Q):
    for tt in range(Q):
        temp.insert(Ans[item][tt],abc[tt])
    text.append(temp)
    temp = []
    
print(''.join(text[R-1]))
