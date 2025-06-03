num = int(input())

family = []

for i in range(num-1):
    fam = list(map(int,input().split()))
    family.append(fam)

#print(len(family))

big = []
samil = []

for j in range(len(family)-1):
    if family[j][0] == 0:
        aa = list(map(int,str(family[j][1])))
        big.append(aa)        
for k in range(len(big)):
    for j in range(len(family)):
        if family[j][0] == big[k][0]:            
            big[k].append(family[j][1])






print(big)




