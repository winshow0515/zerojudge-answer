#AC
from collections import defaultdict, deque
n = int(input())
D = defaultdict(list)#每一個點的鄰居
boss = [None]*(n)#每一個點的祖先

while True:
    try:
        a, b = list(map(int, input().split()))
        D[a].append(b)
        D[b].append(a)
        boss[b] = a
    except EOFError:
        break


def BFS(start):
    Q = deque([(start, 0)]) #節點，距離
    visit = set()
    visit.add(start)
    max_node = None
    max_d = 0
    while Q:
        cur, d = Q.popleft()

        if max_d < d:
            max_node = cur
            max_d = d
        #擴散
        for nxt in D[cur]:
            if nxt in visit:
                continue
            visit.add(cur)
            Q.append((nxt, d+1))
    return max_node, max_d


#從祖先BFS找最遠的點
a, _ = BFS(boss.index(None))
print('a =',a)
#再從那點BFS找最遠的點，則兩點距離為直徑
b, d = BFS(a)
print('b =',b, 'd =', d)