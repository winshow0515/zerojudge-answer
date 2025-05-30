#TLE
n, m = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

dp = [[None]*m for _ in range(n)]
#dp[i][j] = A陣列由0到i和B陣列由0到j的最大內積

def rec(i, j):
    if dp[i][j] != None:
        return dp[i][j]
    if i<0 or j<0:
        return -float('inf')
    dp[i][j] = max(A[i]*B[j], rec(i-1, j-1)+A[i]*B[j])
    return dp[i][j]

ans = rec(n-1, m-1)

dp = [[None]*m for _ in range(n)]
B.reverse()
ans = max(ans, rec(n-1, m-1))
print(ans)