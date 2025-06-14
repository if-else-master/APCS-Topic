n, k = map(int, input().split())
arr = list(map(int, input().split()))

pre = [0] * (n + 1)  # 前綴和
dp = [0] * (n + 1)   # dp[i] 表示前 i 個數中的最大和（限制區間長度不超過 k）

# 計算前綴和
for i in range(1, n + 1):
    pre[i] = pre[i - 1] + arr[i - 1]

dq = []  # 我們用 list 模擬 deque，每個元素是 (index, value)

dq.append((0, 0))  # 初始狀態：第 0 位，值為 0

for i in range(1, n + 1):
    # 把超出範圍 k 的項目從前面移除
    while dq and i - dq[0][0] > k:
        dq.pop(0)

    # 計算當前 dp[i]（從 dq[0] 轉移過來）
    dp[i] = pre[i] - dq[0][1]
    dp[i] = max(dp[i], dp[i - 1])  # 或者不選，繼續沿用之前的最大值

    # 準備更新 dq（要放入 pre[i] - dp[i-1]）
    pb = pre[i] - dp[i - 1]

    # 從後面移除不夠小的值（保持遞增）
    while dq and dq[-1][1] >= pb:
        dq.pop()

    dq.append((i, pb))

print(dp[n])
