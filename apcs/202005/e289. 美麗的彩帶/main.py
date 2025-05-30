from collections import defaultdict, deque
m, n = map(int, input().split())
l = list(map(int, input().split()))
ans = 0
table = defaultdict(int)
uniq = 0
q = deque()

for i in l:
    q.append(i)
    table[i] += 1
    if table[i] == 1:
        uniq += 1
    if len(q) == m+1:
        y = q.popleft()
        table[y] -= 1
        if table[y] == 0:
            uniq -= 1
    if uniq == m:
        ans += 1
print(ans)