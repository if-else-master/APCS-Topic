a = int(input())

num = list(map(int,input().split()))


#0的小圈圈

#i = 0
#me[i] -> num[i] 0 -> 4
#me[num[i]] -> num[me[num[i]]] 4 -> 6
#me[num[me[num[i]]]] -> num[me[num[me[num[i]]]]] 6 -> 8


def fr(num,i,temp=None):
    if temp is None:
        temp = []
    ans = num[i]
    temp.append(num[i])
    if num[i] == 0:
        return temp
    else:
        return fr(num,ans,temp)
    
    
    


aa = fr(num,0)
print(aa)

    
    
