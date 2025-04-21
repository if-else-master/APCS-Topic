number = int(input())
num_list = list(map(int, input().split()))
num_list.insert(0, 0)  # 從 index 1 開始

aa = len(num_list)
max_num = []
min_num = []


for i in range(1, aa - 1):  # i 從 1 到倒數第2個
    for j in range(i + 1, aa):  # j 在 i 之後
        if num_list[i] + num_list[j] == num_list[-1]:
            #print(num_list[i], num_list[j])
            min_num.insert(i-1,num_list[i])
            max_num.insert(-i,num_list[j])

print(max_num)
print(min_num)
