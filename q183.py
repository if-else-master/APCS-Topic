number = int(input())
num_list = list(map(int, input().split()))
num_list.insert(0, 0)  
num_list = list(set(num_list))
aa = len(num_list)
max_num = []
min_num = []
temp = 0
max_temp = num_list[-1]


for i in range(number):
    temp = temp + num_list[i]
    min_num.append(temp)

for j in range(number):
    max_temp = max_temp - num_list[j]
    max_num.append(max_temp)

print(' '.join(map(str,min_num)))
print(' '.join(map(str,sorted(max_num))))
