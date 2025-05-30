#AC
import sys
sys.setrecursionlimit(100000)


n, m = map(int, input().split())
grid = []
for _ in range(n):
    grid.append(list(map(int, input().split())))
dp = [[[None]*m for _ in range(n)] for _ in range(3)]


def rec(i, j, d):
    if i == n or j<0 or j==m:
        return 0
    if i == -1:
        return max(rec(i, j+1, d), rec(i+1, j, 2))
    if dp[d][i][j] != None:
        return dp[d][i][j]
    
    if d == 0:
        ans =  max(rec(i, j+1, d), rec(i+1, j, 2))
    elif d == 1:
        ans = max(rec(i, j-1, d), rec(i+1, j, 2))
    else:
        ans =  max(rec(i, j+1, 0), rec(i, j-1, 1), rec(i+1, j, 2))

    dp[d][i][j] = ans + grid[i][j]
    return dp[d][i][j]


for i in range(n, -1, -1):
    for d in range(3):
        rec(i, 0, d)
        rec(i, m, d)
print(rec(-1, 0, 0))