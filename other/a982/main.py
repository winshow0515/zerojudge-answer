from collections import deque
DIRS = [[0, 1], [0, -1], [1, 0], [-1, 0]]
n = int(input())
maze = [input() for _ in range(n)]

Q = deque([(1, 1, 1)])

visit = set()
answer = None
while Q:
    x, y, cost = Q.popleft()
    if x == n-2 and y == n-2:
        answer = cost
        break
    if (x, y) in visit:
        continue
    visit.add((x, y))
    for dx, dy in DIRS:
        nx, ny = x + dx, y + dy
        if maze[nx][ny] == ".":
            Q.append((nx, ny, cost+1))

if answer == None:
    print("No solution!")
else:
    print(answer)