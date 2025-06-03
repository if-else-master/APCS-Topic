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

cut = []
many = 0

while del1:  # 當 del1 還有東西時
    tail = del1[0]  # 取第一個差值當參考
    del del1[0]     # 把它刪掉

    n = 0
    while n < len(del1):
        if del1[n] == tail:
            del del1[n]  # 不要 n += 1，因為刪掉了元素後 index 前移
        else:
            cut.append(del1[n])
            many += del1[n]
            del del1[n]
            break  # 跳出這輪內層 while，回到外層重新來
    # 如果內層 while 正常跑完，會自動再跑一次外層 while



ans = max(num_list) - min(num_list) - many

print(cut)

