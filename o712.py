M, N, j, r, c = list(map(int, input().split()))
MN_list = []
pass_list = []
ans = []

for i in range(M):
    MN = list(map(int, input().split()))
    if len(MN) != N:
        print("錯誤")
        break
    MN_list.append(MN)

temp = MN_list[r][c]
tmp = 1
dam = 0

while tmp != 0:
    if MN_list[r][c] == 0:  # 如果當前格子的寶石數量為 0，終止
        break

    k = 1
    # 如果當前格子可行且不等於 -1，且temp 不是 j 的倍數，則繼續
    if c + k < N and MN_list[r][c + k] != -1 and temp % j != 0:
        tmp = MN_list[r][c + k]
        temp = temp + MN_list[r][c + k]                
        ans.append(temp)
        pass_list.append(MN_list[r][c + k])
        MN_list[r][c + k] = MN_list[r][c + k] - 1
        r = r
        c = c + k
        dam += 1
    else:
        # 如果 temp 是 j 的倍數，向右轉 90 度（只改變檢查順序）
        if temp % j == 0:
            # 嘗試四個方向，右、下、左、上
            for _ in range(4):
                if c + k < N and MN_list[r][c + k] != -1:  # 向右
                    tmp = MN_list[r][c + k]
                    temp = temp + MN_list[r][c + k]                
                    ans.append(temp)
                    pass_list.append(MN_list[r][c + k])
                    MN_list[r][c + k] = MN_list[r][c + k] - 1
                    r = r
                    c = c + k
                    dam += 1
                    break
                elif r + k < M and MN_list[r + k][c] != -1:  # 向下
                    tmp = MN_list[r + k][c]
                    temp = temp + MN_list[r + k][c]        
                    ans.append(temp)
                    pass_list.append(MN_list[r + k][c])
                    MN_list[r + k][c] = MN_list[r + k][c] - 1
                    r = r + k
                    c = c
                    dam += 1
                    break
                elif c - k >= 0 and MN_list[r][c - k] != -1:  # 向左
                    tmp = MN_list[r][c - k]
                    temp = temp + MN_list[r][c - k]     
                    ans.append(temp)
                    pass_list.append(MN_list[r][c - k])
                    MN_list[r][c - k] = MN_list[r][c - k] - 1
                    r = r
                    c = c - k
                    dam += 1
                    break
                elif r - k >= 0 and MN_list[r - k][c] != -1:  # 向上
                    tmp = MN_list[r - k][c]
                    temp = temp + MN_list[r - k][c]        
                    ans.append(temp)
                    pass_list.append(MN_list[r - k][c])
                    MN_list[r - k][c] = MN_list[r - k][c] - 1
                    r = r - k
                    c = c
                    dam += 1
                    break
            else:
                # 四個方向都無法走，結束
                break

print(dam)
print(ans)
print(pass_list)
