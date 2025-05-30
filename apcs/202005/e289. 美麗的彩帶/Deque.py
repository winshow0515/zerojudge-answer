from collections import deque, defaultdict
m, n = map(int, input().split())
L = list(map(int, input().split()))

table = defaultdict(int)
uniq = 0
q = deque()
ans = 0
for x in L:
    q.append(x)
    table[x] += 1
    if table[x] == 1:
        uniq += 1
    if len(q) == m+1:
        y = q.popleft()
        table[y] -= 1
        if table[y] == 0:
            uniq -= 1
    if uniq == m:
        ans += 1
print(ans)