from collections import deque

def distance(a, b, c, d):
    return abs(a-c) + abs(b-d)

n, m = map(int, input().split())
A = [list(map(int,input().split())) for _ in range(n)]
special = []
for i in range(n):
    for j in range(m):
        #用BFS
        count = 0
        Q = deque([(i,j)])
        visit = set()
        while Q:
            x, y = Q.popleft()
            if not(0 <= x < n and 0 <= y < m):
                continue
            if (x,y) in visit:
                continue
            visit.add((x,y))
            if distance(i, j, x, y) <= A[i][j]:
                count += A[x][y]
                for dx, dy in [[1,0],[0,1],[-1,0],[0,-1]]:
                    nx, ny = x+dx, y+dy
                    Q.append((nx, ny))
        if count % 10 == A[i][j]:
            special.append((i, j))
print(len(special))
for x, y in special:
    print(x, y)