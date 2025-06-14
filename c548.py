a,b = map(int,input().split())

num = list(map(int,input().split()))

number = []
temp =0

for i in range(a):
    temp = temp + num[i]
    for j in range(i+1,a):
        temp = temp + num[j]
        number.append(temp)
    temp = 0

ans = 0

for k in range(len(number)):
    if number[k] % b == 0:
        ans = number[k]

#print(ans)
ans2 = []
ans3 = []

for u in range(a):
    temp = temp + num[u]
    ans2.append(u)
    for g in range(u+1,a):
        temp = temp + num[g]
        ans2.append(g)
        if temp == ans:
            ans3 = ans2
            break
    ans2 = []
    temp = 0

print(len(ans3))
for o in range(len(ans3)):
    ans3[o] = ans3[o]+1
print(' '.join(map(str,ans3)))
