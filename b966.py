number = int(input())

num_list = []

for i in range(number):
    one,two = map(int,input().split())
    for j in range(one,two+1):
        if j not in num_list:
            num_list.append(j)
            
num_list.sort()
del1 = []

for k in range(len(num_list)-1):
    aa = num_list[k+1] - num_list[k]
    del1.append(aa)

unique = set(del1)
most_common = max(unique, key=del1.count)

# 移除所有該元素
del1 = [x for x in del1 if x != most_common]

ans = max(num_list) - min(num_list)
for n in range(len(del1)):
    ans = ans - del1[n]


print(ans)
