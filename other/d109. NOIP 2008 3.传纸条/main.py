m, n = map(int, input().split())
grid = [list(map(int,input().split())) for _ in range(m)]

dp = {}

def rec(x1, y1, x2, y2):
    if x1==x2==y1==y2==0:
        return 0
    if x1==x2 and y1 == y2:
        return -float('inf')
    if x1<0 or x2<0 or y1<0 or y2<0:
        return -float('inf')
    if (x1, y1, x2, y2) not in dp:
        dp[x1, y1, x2, y2] = max(
            rec(x1-1, y1, x2-1, y2),
            rec(x1-1, y1, x2, y2-1),
            rec(x1, y1-1, x2-1, y2),
            rec(x1, y1-1, x2, y2-1)
        ) + grid[x1][y1] + grid[x2][y2]
    return dp[x1, y1, x2, y2]

print(rec(m-1,n-2,m-2,n-1))