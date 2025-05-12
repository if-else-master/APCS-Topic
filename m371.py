n, m = map(int, input().split())
m1 = []
ans = 0

for i in range(n):
    m1.append(list(map(int, input().split())))
aa = 0
while aa <= 1000:
    # 左右相同的數（允許中間有 None）
    for j in range(n):
        h = 0
        while h < m - 1:
            if m1[j][h] is None:
                h += 1
                continue
            k = h + 1
            while k < m and m1[j][k] is None:
                k += 1
            if k < m and m1[j][h] == m1[j][k]:
                ans += m1[j][k]
                m1[j][h] = None
                m1[j][k] = None
                h = k + 1  # 跳到後面避免重複
            else:
                h += 1

    # 上下相同的數（允許中間有 None）
    for h in range(m):
        j = 0
        while j < n - 1:
            if m1[j][h] is None:
                j += 1
                continue
            k = j + 1
            while k < n and m1[k][h] is None:
                k += 1
            if k < n and m1[j][h] == m1[k][h]:
                ans += m1[k][h]
                m1[j][h] = None
                m1[k][h] = None
                j = k + 1
            else:
                j += 1
    aa += 1

print(ans)
