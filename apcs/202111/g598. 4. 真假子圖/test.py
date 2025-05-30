from collections import deque

#輸入
n, m = map(int, input().split())
g0 = [[] for _ in range(n)]#組長有的原始圖
inp = list(map(int, input().split()))
for i in range(0, 2*m, 2):
    g0[inp[i]].append(inp[i+1])
    g0[inp[i+1]].append(inp[i])

p, k = map(int, input().split())
gi = []
for i in range(p):
    gi.append(list(map(int, input().split())))



def bipartite(G):
    def dfs(start, num):    #把dfs()放在bipar()裡面，這樣就不用把G, group傳來傳去
        stack = deque([(start, num)])
        while stack:
            cur, cur_n = stack.popleft()
            if group[cur] != 0:
                if group[cur] != cur_n:
                    return False
                continue
            group[cur] = cur_n
            for nxt in G[cur]:
                stack.append((nxt, 3-cur_n))
        return True

    group = [0]*n   #0,1,2
    for i in range(n):#因為不是所有點都連通
        if group[i]==0:
            if not dfs(i, 1):
                return False
    return True





#g0+gi[i]
for i in range(p):
    G = [edge[:] for edge in g0]
    for j in range(0, 2*k, 2):
        G[gi[i][j]].append(gi[i][j+1])
        G[gi[i][j+1]].append(gi[i][j])
    #check
    if not bipartite(G):
        print(i+1)
        