x,n = map(int,input().split())
map_list = sorted(list(map(int, input().split())))
ans = 0
ans2 = 0



for i in range(20):
    if x >= map_list[-1]:
        map_list.append(x)
        ans = n
        ans2 = map_list[0]
        break
    if x <= map_list[i]:
        map_list.insert(i,x)
        if n - i > i:
            ans = n-i
            ans2 = map_list[-1]
        else:
            ans = i
            ans2 = map_list[0]
        break
    else:
        continue



print(ans,ans2)





