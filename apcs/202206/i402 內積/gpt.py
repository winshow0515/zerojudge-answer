n, m = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# 初始化 DP 表
dp = [[-float('inf')] * (m + 1) for _ in range(n + 1)]

# 填表
ans = -float('inf')  # 儲存全域最大值
for i in range(1, n + 1):
    for j in range(1, m + 1):
        # 計算 dp[i][j]
        dp[i][j] = max(
            A[i - 1] * B[j - 1],           # 單獨內積
            dp[i - 1][j - 1] + A[i - 1] * B[j - 1]  # 延續內積
        )
        # 更新答案
        ans = max(ans, dp[i][j])

# 反向計算
B.reverse()
# 重置 DP 表
dp = [[-float('inf')] * (m + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        dp[i][j] = max(
            A[i - 1] * B[j - 1],
            dp[i - 1][j - 1] + A[i - 1] * B[j - 1]
        )
        ans = max(ans, dp[i][j])

print(ans)
