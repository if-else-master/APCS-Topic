num = int(input())

family = []

for i in range(num - 1):
    fam = list(map(int, input().split()))
    family.append(fam)

print(family)
