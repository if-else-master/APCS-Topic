num = int(input())
map_list = []

for i in range(num):
    aa = list(map(int,input().split()))
    map_list.append(aa)

#print(map_list)

#[1][0] - [0][0]
#[1][1] - [0][1]
#[2][0] - [1][0]
#[2][1] - [1][1]

ans = []

for j in range(len(map_list)-1):
    temp = abs(map_list[j+1][0] - map_list[j][0])
    temp2 = abs(map_list[j+1][1] - map_list[j][1])
    ans.append(temp+temp2)


print(max(ans),min(ans))
