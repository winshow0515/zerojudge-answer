#TLE了，這題python過不了
from collections import defaultdict
m, n = map(int, input().split())

table = defaultdict(int)
lt = set()
for i in range(n):
    tmp = "".join(sorted(set(input())))
    table[tmp] += 1
    lt.add(tmp)
lt = list(lt)

ans = 0
for i in range(len(lt)):
    a = lt[i]
    for j in range(i+1, len(lt)):
        b = lt[j]
        if not set(a)&set(b) and len(a)+len(b)==m:
            ans += table[a]*table[b]
#print(ans^)