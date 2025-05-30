from collections import deque, defaultdict
m, n = map(int, input().split())
L = list(map(int, input().split()))
table = defaultdict(int)
uniq = 0
for i in range(m):
    table[L[i]] += 1
    if table[L[i]] == 1:
        uniq += 1
ans = int(uniq == m)
for i in range(m+1, n):
    table[L[i-m-1]] -= 1
    if table[L[i-m-1]] == 0:
        uniq -= 1
    table[L[i]] += 1
    if table[L[i]] == 1:
        uniq += 1
    if uniq == m:
        ans += 1
        break