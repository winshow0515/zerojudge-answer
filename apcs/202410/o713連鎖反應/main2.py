#AC
from collections import deque, defaultdict
#輸入
m, n, q = map(int,input().split())
graph = []
for i in range(m):
    temp = list(map(int, input().split()))
    for j in range(n):
        if temp[j] == -2:
            start_x = i
            start_y = j
    graph.append(temp)

#前置處理
d = defaultdict(list) #放置由起點擴散r格能碰到的點
visit1 = {(start_x, start_y)}
Q = deque([(start_x, start_y, 0)])
while Q:
    x, y, r = Q.popleft()
    visit1.add((x, y))
    d[r].append((x, y))
    for dx, dy in [[0, 1],[0, -1],[1, 0],[-1, 0]]:
        nx, ny = x+dx, y+dy
        if not (0<=nx<m and 0<=ny<n) or (nx, ny) in visit1 or graph[nx][ny]<0:
            continue

        visit1.add((nx, ny))
        Q.append((nx, ny, r+1))

#bfs
visit2 = {(start_x, start_y) : 0}
for ans in range(1, m*n+1):
    Q = deque(d[ans])#這是由起點觸發的格子還有中途開始連鎖的炸彈
    
    while Q:
        x, y = Q.popleft()
        Q2 = deque([(x, y, graph[x][y])])#這是觸發連鎖的炸彈的擴散
        while Q2:
            x2, y2, r2 = Q2.popleft()
            if ((x2,y2) not in visit2 or r2 > visit2[x2, y2]) and r2>=0:
                visit2[x2, y2] = r2
                if r2 > 0:
                    for dx, dy in [[0, 1],[0, -1],[1, 0],[-1, 0]]:
                        nx, ny = x2+dx, y2+dy
                        if not (0<=nx<m and 0<=ny<n) or graph[nx][ny]==-1:
                            continue
                        Q2.append((nx, ny, r2-1))
                        if graph[nx][ny]>0:
                            Q.append((nx, ny))
    
    if len(visit2) >= q:
        print(ans)
        break