M, N, j, r, c = list(map(int, input().split()))
MN_list = []
for i in range(M):
    MN = list(map(int, input().split()))
    if len(MN) != N:
        print("錯誤")
        break
    MN_list.append(MN)

#格子的數值-1 lat -1
#格子數值相加 lat + lat score
#走過要+1 dam

lat = MN_list[r][c]
score = 0
dam = 0
pass_list = []
pass_list.append(lat)
MN_list[r][c] = lat-1
score = score+lat
dam+=1

while lat != 0:
    if c+1<N and MN_list[r][c+1] != -1 and score%j !=0:
        lat = MN_list[r][c+1]
        pass_list.append(MN_list[r][c+1])
        score = score+MN_list[r][c+1]
        if MN_list[r][c+1] > 0:
            MN_list[r][c+1] = lat-1
            dam+=1
        r = r
        c = c+1
        #print(pass_list,"a")
    else:
        for _ in range(4):
            if r+1<M and MN_list[r+1][c] != -1:
                while r+1<M and MN_list[r+1][c] != -1:
                    lat = MN_list[r+1][c]
                    pass_list.append(MN_list[r+1][c])
                    score = score+MN_list[r+1][c]
                    if MN_list[r+1][c] > 0:
                        MN_list[r+1][c] = lat-1
                        dam+=1
                    r = r+1
                    c = c
                    #print(pass_list,"b")
            elif c-1>=0 and MN_list[r][c-1] != -1:
                while c-1>=0 and MN_list[r][c-1] != -1:
                    lat = MN_list[r][c-1]
                    pass_list.append(MN_list[r][c-1])
                    score = score+MN_list[r][c-1]
                    if MN_list[r][c-1] > 0:
                        MN_list[r][c-1] = lat-1
                        dam+=1            
                    r = r
                    c = c-1
                    #print(pass_list,"c")
            elif r-1>=0 and MN_list[r-1][c] != -1:
                while r-1>=0 and MN_list[r-1][c] != -1:
                    lat = MN_list[r-1][c]
                    pass_list.append(MN_list[r-1][c])
                    score = score+MN_list[r-1][c]
                    if MN_list[r-1][c] > 0:
                        MN_list[r-1][c] = lat-1
                        dam+=1
                    r = r-1
                    c = c
                    #print(pass_list,"d")
    
print(dam)
#print(pass_list)
