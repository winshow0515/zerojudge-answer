#RecursionError: maximum recursion depth exceeded in comparison

n, m = map(int, input().split())
grid = []
for _ in range(n):
    grid.append(list(map(int, input().split())))
dp_r = [[None]*m for _ in range(n)]
dp_l = [[None]*m for _ in range(n)]

def rec_r(i, j):
    if dp_r[i][j] != None:
        return dp_r[i][j]
    
    right = rec_r(i, j+1) if j+1 < m else -float('inf')
    down = max(rec_r(i+1, j), rec_l(i+1, j)) if i+1 < n else 0
    dp_r[i][j] = max(right, down) + grid[i][j]
    return dp_r[i][j]

def rec_l(i, j):
    if dp_l[i][j] != None:
        return dp_l[i][j]
    
    left = rec_l(i, j-1) if j-1 > -1 else -float('inf')
    down = max(rec_r(i+1, j), rec_l(i+1, j)) if i+1 < n else 0
    dp_l[i][j] = max(left, down) + grid[i][j]
    return dp_l[i][j]

rec_r(0, 0)
rec_l(0, m-1)
print('dp_r')
for i in range(n):
    print(dp_r[i])
print('')
print('dp_l')
for i in range(n):
    print(dp_l[i])
ans = -float('inf')
for i in range(m):
    ans = max(ans, dp_r[0][i], dp_l[0][i])
print(ans)