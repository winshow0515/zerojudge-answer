#TLE
from collections import deque
import sys
#輸入
m, n, q = map(int,sys.stdin.readline().split())
graph = []
for i in range(m):
    temp = list(map(int, sys.stdin.readline().split()))
    for j in range(n):
        if temp[j] == -2:
            start_x = i
            start_y = j
    graph.append(temp)



def bfs(start_r):
    Q = deque([(start_x, start_y, start_r)])
    visit = [[None]*n for _ in range(m)]
    visit[start_x][start_y] = start_r
    count = 1
    while Q:
        #print(Q)
        x, y, r = Q.popleft()
        
        if r > 0:
            for dx, dy in [(0,1),(1,0),(0,-1),(-1,0)]:
                nx, ny = x+dx, y+dy
                if not(0<=nx<m and 0<=ny<n):
                    continue
                if graph[nx][ny] == -1:
                    continue

                if visit[nx][ny] != None:
                    if r-1 > visit[nx][ny]: 
                        Q.append((nx, ny, r-1))
                        visit[nx][ny] = r-1
                else:
                    Q.append((nx, ny, max(r-1, graph[nx][ny])))
                    visit[nx][ny] = max(r-1, graph[nx][ny])
                    count += 1
        
    return count >= q

'''
print(bfs(500))
'''
#二分搜
left = 0
right = n*m

while left<right:
    mid = (left+right)//2
    if bfs(mid):
        right = mid
    else:
        left = mid+1

print(left)