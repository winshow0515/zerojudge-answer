#TLE
from collections import deque
#input
n, m = map(int,input().split())

graph = [input() for _ in range(n)]

#F:右和下 H:左和右 7:左和下 I:上和下 L:右和上 J:左和上 X:上、下、左和右
#右(0, 1) 下(1, 0) 左(0,-1) 下(1, 0)
D = {
    ('F', (0, 1)): 'H7XJ',
    ('F', (1, 0)): 'IXLJ',
    ('H', (0,-1)): 'HFXL',
    ('H', (0, 1)): 'H7XJ',
    ('7', (0,-1)): 'FHXL',
    ('7', (1, 0)): 'IXLJ',
    ('I', (-1,0)): 'IF7X',
    ('I', (1, 0)): 'IXLJ',
    ('L', (-1,0)): 'IF7X',
    ('L', (0, 1)): 'H7XJ',
    ('J', (-1,0)): 'IF7X',
    ('J', (0,-1)): 'FHXL',
    ('X', (0,-1)): 'FHXL',
    ('X', (0, 1)): 'H7XJ',
    ('X', (-1,0)): 'IF7X',
    ('X', (1, 0)): 'IXLJ'}


ans = 0
visit = set()
for i in range(n):
    for j in range(m):
        if graph[i][j] != 0:
            #DFS
            count = 0
            
            if (i, j) in visit:
                continue
            visit.add((i, j))
            stack = deque([(i, j)])

            while stack:
                x, y = stack.pop()
                count += 1
                for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                    nx, ny = x+dx, y+dy

                    if not(0 <= nx < n and 0 <= ny <m) or graph[nx][ny] == 0 or (nx, ny) in visit:
                        continue

                    if (graph[x][y], (dx, dy)) in D:
                        if graph[nx][ny] in D[(graph[x][y], (dx, dy))]:#合法
                            stack.append((nx, ny))
                            visit.add((nx, ny))#至關重要的一行少了就TLE
                            
            ans = max(ans, count)
print(ans)