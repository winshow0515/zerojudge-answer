#AC
n, m = map(int, input().split())
grid = []
for _ in range(n):
    grid.append(list(map(int, input().split())))
dp_r = [[None]*m for _ in range(n)]
dp_l = [[None]*m for _ in range(n)]

for i in range(n):
    for j in range(m):
        jl = m-j-1
        if i == 0:
            dp_r[i][j] = grid[i][j] if j == 0 else max(grid[i][j], dp_r[i][j-1]+grid[i][j])
            dp_l[i][jl] = grid[i][jl] if j == 0 else max(grid[i][jl], dp_l[i][jl+1]+grid[i][jl])
        else:
            if j == 0:
                dp_r[i][j] = max(dp_r[i-1][j], dp_l[i-1][j])+grid[i][j]
                dp_l[i][jl] = max(dp_r[i-1][jl], dp_l[i-1][jl])+grid[i][jl]
            else:
                dp_r[i][j] = max(dp_r[i-1][j], dp_l[i-1][j], dp_r[i][j-1])+grid[i][j]
                dp_l[i][jl] = max(dp_r[i-1][jl], dp_l[i-1][jl], dp_l[i][jl+1])+grid[i][jl]

#print(dp_r)
#print(dp_l)
print(max(*dp_r[-1], *dp_l[-1]))