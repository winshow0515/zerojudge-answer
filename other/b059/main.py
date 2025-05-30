from collections import deque
from sys import stdin
DIRS = [[3,1],[3,-1],[-3,1],[-3,-1],[1,3],[-1,3],[1,-3],[-1,-3]]

while True:
    n = int(input())
    if not n:
        break
    board = [['.']*100 for _ in range(100)]
    for i in range(n):
        x, y = map(int, input().split())
        board[x][y] = '#'

    dog_x, dog_y = map(int, input().split())
    target_x, target_y = map(int, input().split())
    flag = False
    #BFS
    Q = deque([(dog_x, dog_y, 0)])
    while Q:
        x, y, cost = Q.popleft()
        if (x, y) == (target_x, target_y):
            print(cost)
            flag = True
            break
        board[x][y] = '@' #走過作記號阿
        for dx, dy in DIRS:
            nx, ny = x+dx, y+dy
            
            #邊界
            if nx < 0 or nx > 98 or ny < 0 or ny > 98:
                continue
            if board[nx][ny] == '.':
                if dx == 3 and board[x+1][y] == '.':
                    Q.append((nx, ny, cost+1))
                if dx == -3 and board[x-1][y] == '.':
                    Q.append((nx, ny, cost+1))
                if dy == 3 and board[x][y+1] == '.':
                    Q.append((nx, ny, cost+1))
                if dy == -3 and board[x][y-1] == '.':
                    Q.append((nx, ny, cost+1))
    if not flag:
        print("impossible")