num = int(input())

family = []

for i in range(num-1):
    fam = list(map(int,input().split()))
    family.append(fam)

print(len(family))
ans = []



for j in range(len(family)):
    for k in range(len(family)):
        if family[j][1] == family[k][0] and family[j][1] != 0:
            print(family[k],family[j][1],family[k][0])
            family[j].append(family[k][1])
            ans.append(family[j])


print(ans)
cut = []

for item in ans:
    if item not in cut:
        cut.append(item)

print(cut)



#print(family[0][1],family[4][0])
#[[0, 1], [0, 2], [0, 3], [7, 0], [1, 4], [1, 5], [3, 6]]
