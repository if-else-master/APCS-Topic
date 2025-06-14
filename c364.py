num = int(input())
b = []

bed = []

for i in range(num):
    b.append(list(map(int,input().split())))

for j in range(num):
    if j == 0:
        while b[j] > b[j+1]:
            bed.append(b[j+1])
            print(bed)

for k in range(num,0,-1):
    if j != 0 and j != num:
        while b[k] > b[k-1]:
            bed.append(b[k-1])
            print(bed)

for u in range(num):
    if u != 0 and u != num:
        while b[u] > b[u-1]:
            bed.append(b[u-1])
        while b[u] > b[u+1]:
            bed.append(b[u+1])
            print(bed)

print(sum(bed))
        
        
        
