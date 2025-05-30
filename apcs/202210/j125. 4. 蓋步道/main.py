from collections import deque
def main():
    n = int(input())
    graph = [list(map(int, input().split())) for _ in range(n)]

    #找最短路
    def bfs(h):
        Q = deque([(0, 0, 0)]) #(t, x, y)
        visit = [[False]*n for _ in range(n)]
        while Q:
            t, x, y = Q.popleft()
            if (x, y) == (n-1, n-1):
                return True, t
            for dx, dy in [(0,1),(0,-1),(1,0),(-1,0)]:
                nx, ny = x+dx, y+dy
                if not (0<= nx < n and 0<= ny < n):#出界
                    continue
                if visit[nx][ny]:#重複
                    continue
                if abs(graph[x][y]-graph[nx][ny]) > h:
                    continue
                Q.append((t+1, nx, ny))
                visit[nx][ny] = True
        return False, -1

    #對答案二分搜最小高度差
    l, r = 1, 10**6
    while l<r:
        mid = (l+r)//2
        temp = bfs(mid)
        if not temp[0]:#mid太小
            l = mid+1
        else:
            r = mid

    print(l)
    temp = bfs(l)
    print(temp[1])
main()