#TLE
n, m = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

dp = [[None]*(m+1) for _ in range(n+1)]
#dp[i][j] = A陣列由0到i和B陣列由0到j的最大內積
ans = -float('inf')
for i in range(n+1):
    dp[i][0] = -float('inf')
for j in range(m+1):
    dp[0][j] = -float('inf')

for i in range(1,n+1):
    for j in range(1,m+1):
        dp[i][j] = max(A[i-1]*B[j-1], dp[i-1][j-1]+A[i-1]*B[j-1])
        ans = max(ans, dp[i][j])


B.reverse()
dp = [[None]*(m+1) for _ in range(n+1)]

for i in range(n+1):
    dp[i][0] = -float('inf')
for j in range(m+1):
    dp[0][j] = -float('inf')

for i in range(1,n+1):
    for j in range(1,m+1):
        dp[i][j] = max(A[i-1]*B[j-1], dp[i-1][j-1]+A[i-1]*B[j-1])
        ans = max(ans, dp[i][j])

print(ans)