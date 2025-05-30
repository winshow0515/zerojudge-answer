#AC
from collections import deque
#bfs
n, P, L, R = map(int, input().split())
S = list(map(int, input().split()))
Q = deque([(0, 0)])#(位置cur, 次數t)
visit = set()
ans = -1
while Q:
    cur, t = Q.popleft()
    if cur == P:
        ans = t
        break
    visit.add(cur)
    #左右走走看
    if cur-L >= 0 and 0<=S[cur-L]<n and (S[cur-L] not in visit):
        Q.append((S[cur-L], t+1))
        visit.add(S[cur-L])
    if cur+R < n and 0<=S[cur+R]<n and (S[cur+R] not in visit):
        Q.append((S[cur+R], t+1))
        visit.add(S[cur+R])

print(ans)